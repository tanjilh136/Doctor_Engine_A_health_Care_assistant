import tkinter as tk
from image_class import ImageClass
from tkinter import filedialog
import functions
from tkinter import ttk
import predict

root = tk.Tk()
root.geometry("800x600")
root.resizable(width='false', height='false')

main_frame = tk.Frame(root, background='lightblue')
main_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

imagePath = tk.StringVar()


def choose_image(display_frame, result_frame):
    image_path = tk.filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])
    functions.clearFrame(display_frame)
    functions.clearFrame(result_frame)

    try:
        e = ImageClass(display_frame, image_path)
        e.pack(fill='both', expand='yes')
    except AttributeError:
        pass

    imagePath.set(image_path)


print(imagePath.get())


def image_page(image_page_frame):
    functions.clearFrame(image_page_frame)

    s = ttk.Style()
    s.configure('TFrame')

    image_page_upper_frame = ttk.Frame(image_page_frame, )
    image_page_upper_frame.place(relx=0, rely=0, relwidth=1, relheight=0.20)

    image_page_labels(image_page_upper_frame)

    image_page_middle_frame = ttk.Frame(image_page_frame, )
    image_page_middle_frame.place(relx=0, rely=.20, relwidth=1, relheight=.65)

    selected_image = ttk.Label(image_page_middle_frame, text='Selected Image')
    selected_image.place(relx=0.2, )

    s.configure('image_page_image_frame.TFrame', background='white', )
    image_page_image_frame = ttk.Frame(image_page_middle_frame, style='image_page_image_frame.TFrame')
    image_page_image_frame.place(relx=0.025, rely=0.09, relwidth=0.5, relheight=0.9)

    image_page_result_frame = ttk.Frame(image_page_middle_frame, )
    image_page_result_frame.place(relx=0.595, relwidth=0.375, relheight=1)

    image_page_lower_frame = ttk.Frame(image_page_frame, )
    # image_page_lower_frame.config(highlightbackground="gray", highlightcolor="gray")
    image_page_lower_frame.place(rely=.85, relwidth=1, relheight=0.15)

    """ 
    below in the select_image_button, the function for choosing inage is used, 
    but as fas as I know, we can not get a return from the 'command=lambda : [functions.choose_image(imagePage_image_frame)]', 
    if we can get a return, then we can use the file path to process to image detection and the result page.
    """

    select_image_button = ttk.Button(image_page_lower_frame, text='Select image',
                                     command=lambda: [choose_image(image_page_image_frame, image_page_result_frame)])
    select_image_button.pack(padx=60, side='left')

    submit_image_button = ttk.Button(image_page_lower_frame, text='Submit image',
                                     command=lambda: [result_page(image_page_result_frame, imagePath.get())])
    submit_image_button.pack(padx=60, side='right')


def image_page_labels(frame):
    doctor_engine = tk.Label(frame, text='Doctor Engine', font='Arial 20')
    doctor_engine.place(relx=0.04, rely=0.1)

    instruction = tk.Label(frame, text='*To detect a stroke(brain) press the "Select image" button, then select an image, '

                                       'then press the "Submit button" to see the result')
    instruction.place(relx=0.04, rely=0.5)


# def welcome_page(frame):
#     welcome_page_lower_frame = tk.Frame(frame, highlightthickness=2, bd=10)
#     welcome_page_lower_frame.config(highlightbackground="gray", highlightcolor="gray")
#     welcome_page_lower_frame.place(rely=0.75, relwidth=1, relheight=0.25)
#
#     next_button = tk.Button(welcome_page_lower_frame, text='Next >>', command=lambda: [imagePage(frame)])
#     next_button.pack(side='bottom')


def result_page(result_page_frame, path):
    functions.clearFrame(result_page_frame)
    result1=predict.resultPredict(path)
    print('printing in result page' + result1)

   

    result_page_label = tk.Label(result_page_frame, text=result1,font='Arial 13')
    result_page_label.place(relx=0.04, rely=0.1)


image_page(main_frame)

root.mainloop()
