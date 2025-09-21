from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slider")

# List of image file paths
image_paths = [
    r"C:\Users\HP\Downloads\Telegram Desktop\balerion.jpg",
    r"C:\Users\HP\Downloads\Telegram Desktop\meraxes.webp",
    r"C:\Users\HP\Downloads\Telegram Desktop\vagar.jpg"
]

# Resize of images
image_size = (1080,1080)
images = [Image.open(path). resize(image_size) for path in image_paths]
photos = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo in photos:
        label.config(image=photo)
        root.update()
        time.sleep(5)

slideshow = cycle(photos)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text="Start Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()