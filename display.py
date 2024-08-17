from tkinter import Tk, Label
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Create the main window
def start_display(item_list):
    for item in item_list:
        display(item.name, item.sku, item.pog, item.image, item.pog, item.stock_status)
    

def display(name, sku, pog, img_item, img_pog, stock_status, size=(350, 400)):
    root = Tk()
    root.title(name)

    # Load images from file paths
    try:
        img_item_save = "images/online_image.jpeg"
        fetch_image(img_item, img_item_save)
        img_ITEM = Image.open(img_item_save)
        img_ITEM = img_ITEM.resize(size)  # Resize the image
        img_ITEM = ImageTk.PhotoImage(img_ITEM)
        # File paths for saved images

        img_POG = Image.open("images/" + img_pog + ".jpeg")
        img_POG = img_POG.resize(size)  # Resize the image
        img_POG = ImageTk.PhotoImage(img_POG)
    except Exception as e:
        print(f"Error loading images: {e}")
        return

    # Create Labels for images
    image_label1 = Label(root, image=img_ITEM)
    image_label1.pack(side='left')

    image_label2 = Label(root, image=img_POG)
    image_label2.pack(side='right')

    # Create a Label to display text
    text = f"Name={name}\n SKU={sku}\n POG={pog}\n Stock Status={stock_status}"
    text_label = Label(root, text=text)
    text_label.pack()

    # Start the GUI event loop
    root.mainloop()

# Fetch image from URL and save it temporarily
def fetch_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
    else:
        raise Exception(f"Failed to download image from {url}")

