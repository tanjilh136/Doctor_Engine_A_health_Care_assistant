import tkinter as tk  
from image_class import ImageClass
from tkinter import filedialog 

def clearFrame(selectedFrame): 
    for widget in selectedFrame.winfo_children(): 
        widget.destroy() 

def choose_image (imageFrame):
    image_path = tk.filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])  
    imagePath = image_path
    print(imagePath) 
    clearFrame(imageFrame)  
    e = ImageClass(imageFrame, image_path) 
    e.pack(fill='both', expand='yes') 