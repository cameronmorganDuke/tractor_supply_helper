import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import requests
from IPython.display import Image, display
from tkinter import Tk, Label, PhotoImage



def get_pog(sku):
    # Correct the column name if it has a trailing space
    df = pd.read_csv('Tractor Supple POG - Sheet1.csv')
    pog = df.loc[df['SKU '] == int(sku), 'POG'].values
    
    # Check if pog_working is empty before attempting to access it
    if len(pog) > 0:
        return pog[0]
    else:
        print("No matching SKU found.")
        return "N/A"

    
def get_store(pog):
    try:
        img = mpimg.imread('images/' + pog + '.jpeg')
        return img
    except FileNotFoundError:
        return("N/A")
        
def display_image(pog):
    img = mpimg.imread('images/' + pog + '.jpeg')
    response = requests.get(img)
    display(Image(response.content))
    


# Create the main window
def display(name, sku, pog, img_item, img_pog):
    root = Tk()
    root.title(name)

    # Load images
    img_ITEM = PhotoImage(file="images/" + img_item + ".jpeg")  # Use PNG format for PhotoImage
    img_POG = PhotoImage(file="images/" + img_pog + ".jpeg") # Use PNG format for PhotoImage

    # Create Labels for images
    image_label1 = Label(root, image=img_ITEM)
    image_label1.pack(side='item')

    image_label2 = Label(root, image=img_POG)
    image_label2.pack(side='pog')

    # Create a Label to display text
    text = "Name=" + name + "SKU=" + sku + "POG=" + pog
    text_label = Label(root, text)
    text_label.pack()

    # Start the GUI event loop
    root.mainloop()