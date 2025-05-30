import requests
import tkinter as tk
from tkinter import messagebox, Label, PhotoImage, Button
from PIL import Image, ImageTk
import os

image_path = os.path.join(os.path.dirname(__file__), "images", "image.png")

USER_API = "http://localhost:5000"
ROOM_API = "http://localhost:5001"
RESERVATION_API = "http://localhost:5002"

MAIN_COLOUR = "#5f5d57"
SECONDARY_COLOUR = "#e9ca7a"

class StartWindow:
    def __init__(self, master):
        self.master = master
        master.title("LuxeHalls")
        
        master.geometry("1720x1060")
        master.config(bg=MAIN_COLOUR)

        title_label = Label(master, text="LuxeHalls - правилното място за избор на зала за вашето събитие", font=("Tahoma", 26), fg=SECONDARY_COLOUR, background=MAIN_COLOUR).pack(pady=50)
        
        image_path = os.path.join(os.path.dirname(__file__), "images", "image.png")
        pil_image = Image.open(image_path)

       
        max_width, max_height = 650, 350
        pil_image.thumbnail((max_width, max_height))

        self.background_image = ImageTk.PhotoImage(pil_image)

        image_label = tk.Label(self.master, image=self.background_image, borderwidth=0)
        image_label.pack(pady=50)
        
        login_button = Button(master, text="Вход", width=20, font=("Tahoma", 16), command=self.open_login, background=SECONDARY_COLOUR).pack(pady=30)
        register_button = Button(master, text="Регистрация", width=20, font=("Tahoma", 16), command=self.open_register, background=SECONDARY_COLOUR).pack(pady=30)

    def open_login(self):
        self.master.withdraw()
        login_window = tk.Toplevel()
        #LoginWindow(login_window)

    def open_register(self):
        self.master.withdraw()
        register_window = tk.Toplevel()
        #RegisterWindow(register_window)


if __name__ == "__main__":
    root = tk.Tk()
    StartWindow(root)
    root.mainloop()
