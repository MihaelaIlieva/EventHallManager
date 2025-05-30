import requests
import tkinter as tk
from tkinter import messagebox, Label, PhotoImage, Button, Entry
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
        self.master.title("LuxeHalls")
        
        self.master.geometry("1720x1060")
        self.master.config(bg=MAIN_COLOUR)

        self.title_label = Label(master, text="LuxeHalls - правилното място за избор на зала за вашето събитие", font=("Tahoma", 26), fg=SECONDARY_COLOUR, background=MAIN_COLOUR).pack(pady=50)
        
        image_path = os.path.join(os.path.dirname(__file__), "images", "image.png")
        pil_image = Image.open(image_path)

       
        max_width, max_height = 650, 350
        pil_image.thumbnail((max_width, max_height))

        self.background_image = ImageTk.PhotoImage(pil_image)

        image_label = Label(self.master, image=self.background_image, borderwidth=0)
        image_label.pack(pady=50)
        
        self.login_button = Button(master, text="Вход", width=20, font=("Tahoma", 16), command=self.open_login, background=SECONDARY_COLOUR).pack(pady=30)
        self.register_button = Button(master, text="Регистрация", width=20, font=("Tahoma", 16), command=self.open_register, background=SECONDARY_COLOUR).pack(pady=30)

    def open_login(self):
        
        self.master.withdraw()
        login_window = tk.Toplevel()
        LoginWindow(login_window)

    def open_register(self):
        
        self.master.withdraw()
        register_window = tk.Toplevel()
        RegisterWindow(register_window)

class LoginWindow:
    def __init__(self, master):
        
        self.master = master
        self.master.title("Вход")
        self.master.geometry("1720x1060")
        self.master.config(bg=MAIN_COLOUR)
        
        self.title_label = Label(master, text="LuxeHalls - правилното място за избор на зала за вашето събитие", font=("Tahoma", 26), fg=SECONDARY_COLOUR, background=MAIN_COLOUR).pack(pady=50)
        
        image_path = os.path.join(os.path.dirname(__file__), "images", "image.png")
        pil_image = Image.open(image_path)

       
        max_width, max_height = 650, 350
        pil_image.thumbnail((max_width, max_height))

        self.background_image = ImageTk.PhotoImage(pil_image)

        image_label = Label(self.master, image=self.background_image, borderwidth=0)
        image_label.pack(pady=50)

        self.username_label = Label(master, text="Потребителско име:",font=("Tahoma", 14), fg=SECONDARY_COLOUR , background=MAIN_COLOUR).pack(pady=10)
        self.username_entry = Entry(master, width=20)
        self.username_entry.pack(pady=10)
        
        self.password_label = Label(master, text="Парола:", font=("Tahoma", 14), fg=SECONDARY_COLOUR, background=MAIN_COLOUR).pack(pady=10)
        self.password_entry = Entry(master, width=20, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = Button(master, text="Вход", command=self.login, width=20, font=("Tahoma", 16), background=SECONDARY_COLOUR).pack(pady=20)

    def login(self):
        
        name = self.username_entry.get()
        password = self.password_entry.get()

        # only admin profile
        if name == "mihaela" and password == "mihaela1":
            messagebox.showinfo("Успешен вход", "Добре дошла, админ Mihaela!")
            self.master.destroy()
            #AdminWindow()
            return

        try:
            response = requests.post(f"{USER_API}/login", json={"username": name, "password": password})
            if response.status_code == 200:
                data = response.json()
                messagebox.showinfo("Успешен вход", f"Добре дошъл, {name}!")
                self.master.destroy()
                UserWindow(name, data.get("token"))
            else:
                messagebox.showerror("Грешка", "Невалидни данни за вход")
        except Exception as e:
            messagebox.showerror("Грешка", f"Проблем с връзката към сървъра:\n{e}")

class RegisterWindow:
    def __init__(self, master):
        
        self.master = master
        self.master.title("Вход")
        self.master.geometry("1720x1060")
        self.master.config(bg=MAIN_COLOUR)
        
        self.title_label = Label(master, text="LuxeHalls - правилното място за избор на зала за вашето събитие", font=("Tahoma", 26), fg=SECONDARY_COLOUR, background=MAIN_COLOUR).pack(pady=35)
        
        image_path = os.path.join(os.path.dirname(__file__), "images", "image.png")
        pil_image = Image.open(image_path)

       
        max_width, max_height = 650, 350
        pil_image.thumbnail((max_width, max_height))

        self.background_image = ImageTk.PhotoImage(pil_image)

        image_label = Label(self.master, image=self.background_image, borderwidth=0)
        image_label.pack(pady=35)
        
        self.email_label = Label(master, text="Имейл:",font=("Tahoma", 14), fg=SECONDARY_COLOUR , background=MAIN_COLOUR).pack(pady=10)
        self.email_entry = Entry(master, width=20)
        self.email_entry.pack(pady=10)

        self.username_label = Label(master, text="Потребителско име:",font=("Tahoma", 14), fg=SECONDARY_COLOUR , background=MAIN_COLOUR).pack(pady=10)
        self.username_entry = Entry(master, width=20)
        self.username_entry.pack(pady=10)
        
        self.password_label = Label(master, text="Парола:", font=("Tahoma", 14), fg=SECONDARY_COLOUR, background=MAIN_COLOUR).pack(pady=10)
        self.password_entry = Entry(master, width=20, show="*")
        self.password_entry.pack(pady=10)

        self.register_button = Button(master, text="Регистрация", command=self.register, width=20, font=("Tahoma", 16), background=SECONDARY_COLOUR).pack(pady=20)


    def register(self):
        email = self.email_entry.get()
        name = self.username_entry.get()
        password = self.password_entry.get()

        if not (email and name and password):
            messagebox.showerror("Грешка", "Всички полета са задължителни!")
            return

        try:
            response = requests.post(f"{USER_API}/register", json={
                "username": name,
                "password": password,
                "email": email,
            })
            if response.status_code == 201:
                messagebox.showinfo("Успех", "Регистрацията е успешна.")
                self.master.destroy()
                #UserWindow(name, None)
            else:
                messagebox.showerror("Грешка", f"Неуспешна регистрация: {response.text}")
        except Exception as e:
            messagebox.showerror("Грешка", f"Проблем с връзката към сървъра:\n{e}")

class UserWindow:
    def __init__(self, username, token):
        self.token = token
        self.username = username

        self.window = tk.Toplevel()
        self.window.title("Потребителски панел")
        self.window.geometry("1720x1060")
        self.window.config(bg=MAIN_COLOUR)
        
        self.title_label = Label(self.window, text="LuxeHalls - правилното място за избор на зала за вашето събитие", font=("Tahoma", 26), fg=SECONDARY_COLOUR, background=MAIN_COLOUR).pack(pady=35)
        
        self.greeting_label = Label(self.window, text=f"Добре дошъл, {username}!", font=("Tahoma", 20), fg=SECONDARY_COLOUR, background=MAIN_COLOUR).pack(pady=50)

        
        image_path = os.path.join(os.path.dirname(__file__), "images", "image.png")
        pil_image = Image.open(image_path)
       
        max_width, max_height = 650, 350
        pil_image.thumbnail((max_width, max_height))

        self.background_image = ImageTk.PhotoImage(pil_image)

        image_label = Label(self.window, image=self.background_image, borderwidth=0)
        image_label.pack(pady=50)

        self.get_halls_button = Button(self.window, text="Виж зали", width=20, font=("Tahoma", 16), background=SECONDARY_COLOUR, command=self.load_rooms).pack(pady=20)

        self.get_reservations_button = Button(self.window, text="Виж резервации", width=20, font=("Tahoma", 16), background=SECONDARY_COLOUR, command=self.load_reservations).pack(pady=20)
        
        self.rooms_listbox = tk.Listbox(self.window)
        self.rooms_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        self.window.mainloop()

    def load_rooms(self):
        return


    def load_reservations(self):
        return
    


if __name__ == "__main__":
    root = tk.Tk()
    StartWindow(root)
    root.mainloop()
