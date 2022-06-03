import tkinter as tk  
from image_class import ImageClass
from tkinter import filedialog 
import functions



def choose_image (imageFrame):
    image_path = tk.filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])  
    #imagePath = image_path
   #  print(imagePath) 
    functions.clearFrame(imageFrame)  
    e = ImageClass(imageFrame, image_path) 
    e.pack(fill='both', expand='yes')  


# print(imagePath)
 


def imagePage(image_page_frame): 
    functions.clearFrame(image_page_frame) 

    imagePage_upper_frame = tk.Frame(image_page_frame, background='white',  highlightthickness=2, bd=10) 
    imagePage_upper_frame.config(highlightbackground = "gray", highlightcolor= "gray")
    imagePage_upper_frame.place(relx=0, rely=0, relwidth=1, relheight=0.20) 

    imagePage_middle_frame = tk.Frame(image_page_frame, background='white',  highlightthickness=2, bd=10) 
    imagePage_middle_frame.config(highlightbackground = "gray", highlightcolor= "gray") 
    imagePage_middle_frame.place(relx=0, rely=.20, relwidth=1, relheight=.65)  

    imagePage_image_frame = tk.Frame(imagePage_middle_frame, background='white',  highlightthickness=2) 
    imagePage_image_frame.config(highlightbackground = "gray", highlightcolor= "gray")  
    imagePage_image_frame.place(relx=0.35, rely=0.1, relwidth=0.6, relheight=0.8) 

    imagePage_lower_frame = tk.Frame(image_page_frame, highlightthickness = 2, bd = 10)
    imagePage_lower_frame.config(highlightbackground = "gray", highlightcolor= "gray")
    imagePage_lower_frame.place(rely = .85, relwidth=1, relheight= 0.15)

    """ 
    below in the select_image_button, the function for choosing inage is used, 
    but as fas as I know, we can not get a return from the 'command=lambda : [functions.choose_image(imagePage_image_frame)]', 
    if we can get a return, then we can use the file path to process to image detection and the result page.
    """

    select_image_button = tk.Button(imagePage_lower_frame, text='Select image', command=lambda : [choose_image(imagePage_image_frame)]) 
    select_image_button.pack(side='bottom') 

    submit_image_button = tk.Button(imagePage_lower_frame, text='Submit image', command=lambda : [result_page(image_page_frame, imagePath.get())]) 
    submit_image_button.pack(side='top')


def welcome_page(frame):
    welcomepage_lower_frame = tk.Frame(frame, highlightthickness = 2, bd = 10)
    welcomepage_lower_frame.config(highlightbackground = "gray", highlightcolor= "gray")
    welcomepage_lower_frame.place(rely = 0.75, relwidth=1, relheight= 0.25)

    next_button = tk.Button(welcomepage_lower_frame, text='Next >>', command=lambda : [imagePage(frame)]) 
    next_button.pack(side='bottom')  

def result_page(result_page_frame, path):  
    functions.clearFrame(result_page_frame)  
    print('printing in result page' + path)  

    e = ImageClass(result_page_frame, path) 
    e.pack(fill='both', expand='yes')

    result_page_label = tk.Label(result_page_frame, text=path) 
    result_page_label.pack()
