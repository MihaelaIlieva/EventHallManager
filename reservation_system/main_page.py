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
            AdminWindow()
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
                UserWindow(name, None)
            else:
                messagebox.showerror("Грешка", f"Неуспешна регистрация: {response.text}")
        except Exception as e:
            messagebox.showerror("Грешка", f"Проблем с връзката към сървъра:\n{e}")

# finish user window with making reservations
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
    
class AdminWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Админ панел")
        self.window.geometry("1720x1060")
        self.window.config(bg=MAIN_COLOUR)


        self.greetings_label = Label(self.window, text="Добре дошла, админ Mihaela!", font=("Tahoma", 26), fg=SECONDARY_COLOUR, background=MAIN_COLOUR).pack(pady=10)
        self.subtitle_label = Label(self.window, text="Тук ще можеш да управляваш зали и да виждаш всички резервации.", font=("Tahoma", 20), fg=SECONDARY_COLOUR, background=MAIN_COLOUR).pack(pady=10)

        image_path = os.path.join(os.path.dirname(__file__), "images", "image.png")
        pil_image = Image.open(image_path)

       
        max_width, max_height = 650, 350
        pil_image.thumbnail((max_width, max_height))

        self.background_image = ImageTk.PhotoImage(pil_image)

        image_label = Label(self.window, image=self.background_image, borderwidth=0)
        image_label.pack(pady=50)


        self.get_reservations_button = Button(self.window, text="Добави зала", width=20, font=("Tahoma", 16), background=SECONDARY_COLOUR, command=self.add_hall).pack(pady=20)
        self.get_reservations_button = Button(self.window, text="Редактирай зала", width=20, font=("Tahoma", 16), background=SECONDARY_COLOUR, command=self.edit_hall).pack(pady=20)
        self.get_reservations_button = Button(self.window, text="Премахни зала", width=20, font=("Tahoma", 16), background=SECONDARY_COLOUR, command=self.remove_hall).pack(pady=20)
        self.get_reservations_button = Button(self.window, text="Виж резервации", width=20, font=("Tahoma", 16), background=SECONDARY_COLOUR, command=self.load_reservations).pack(pady=20)
              
        self.window.mainloop()     
        
    def add_hall(self):
        self.window.withdraw()
        self.add_window = tk.Toplevel(self.window)
        self.add_window.title("Добавяне на зала")
        self.add_window.geometry("1720x1060")
        self.add_window.config(bg=MAIN_COLOUR)
        
        self.title_label = Label(self.add_window, text="Добавяне на зала", font=("Tahoma", 26), fg=SECONDARY_COLOUR, background=MAIN_COLOUR).pack(pady=35)
        
        image_path = os.path.join(os.path.dirname(__file__), "images", "image.png")
        pil_image = Image.open(image_path)

       
        max_width, max_height = 650, 350
        pil_image.thumbnail((max_width, max_height))

        self.background_image = ImageTk.PhotoImage(pil_image)

        image_label = Label(self.add_window, image=self.background_image, borderwidth=0)
        image_label.pack(pady=50)
        
        self.hall_name_label = Label(self.add_window,text="Име на зала:",font=("Tahoma", 14), fg=SECONDARY_COLOUR , background=MAIN_COLOUR)
        self.hall_name_label.pack(pady=10)
        self.hall_name_entry = Entry(self.add_window, width=20)
        self.hall_name_entry.pack(pady=10)
        
        self.hall_capacity_label = Label(self.add_window,text="Капацитет:",font=("Tahoma", 14), fg=SECONDARY_COLOUR , background=MAIN_COLOUR)
        self.hall_capacity_label.pack(pady=10)
        self.hall_capacity_entry = Entry(self.add_window, width=20)
        self.hall_capacity_entry.pack(pady=10)
        
        self.add_hall_button = Button(self.add_window, text="Добави", width=20, font=("Tahoma", 16), background=SECONDARY_COLOUR, command=self.submit_add)
        self.add_hall_button.pack(pady=20)
        
    def submit_add(self):
        data = {
                "name": self.hall_name_entry.get(),
                "capacity": self.hall_capacity_entry.get()
            }
                
        try:
            response = requests.post(f"{ROOM_API}/room", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Успешно", "Зала е добавена успешно.")
                self.add_window.destroy()
                AdminWindow()
                
            else:
                messagebox.showerror("Грешка", f"Неуспешно добавяне на зала: {response.text}")
        except Exception as e:
            messagebox.showerror("Грешка", f"Проблем с връзката към сървъра:\n{e}")

    def edit_hall(self):
        
        def load_rooms():
            try:
                response = requests.get(f"{ROOM_API}/room")
                return response.json()
            except Exception as e:
                messagebox.showerror("Грешка", f"Проблем с връзката към сървъра:\n{e}")
                return []
        
        self.window.withdraw()
        
        self.edit_window = tk.Toplevel(self.window)
        self.edit_window.title("Редактиране на зала")
        self.edit_window.geometry("1720x1060")
        self.edit_window.config(bg=MAIN_COLOUR)
        
        self.title_label = Label(self.edit_window, text="Редактиране на зала", font=("Tahoma", 26), fg=SECONDARY_COLOUR, background=MAIN_COLOUR)
        self.title_label.pack(pady=35)
        
        rooms = load_rooms()
        room_var = tk.StringVar(self.edit_window, value="Избери зала")
        options = [f"{r['id']}: {r['name']} (капацитет: {r['capacity']})" for r in rooms]
        room_menu = tk.OptionMenu(self.edit_window, room_var, *options)
        room_menu.config(width=50)
        room_menu.pack(pady=20)
        
        self.name_label = Label(self.edit_window, text="Ново име", font=("Tahoma", 16), fg=SECONDARY_COLOUR, background=MAIN_COLOUR)
        self.name_label.pack(pady=20)
        self.name_entry = Entry(self.edit_window)
        self.name_entry.pack()
        
        self.capacity_label = Label(self.edit_window, text="Нов капацитет", font=("Tahoma", 16), fg=SECONDARY_COLOUR, background=MAIN_COLOUR)
        self.capacity_label.pack(pady=20)
        self.capacity_entry = Entry(self.edit_window)
        self.capacity_entry.pack()
        
        def submit():
            selected = room_var.get()
            room_id = selected.split(":")[0]
            
            data = {
                "name": self.name_entry.get(),
                "capacity": self.capacity_entry.get()
            }
            try:
                response = requests.put(f"{ROOM_API}/rooms/{room_id}", json=data)
                if response.status_code == 200:
                    messagebox.showinfo("Успешно", "Зала е променена успешно.")
                    self.edit_window.destroy()
                    AdminWindow()
                else:
                    messagebox.showerror("Грешка", f"Неуспешно промяна на зала: {response.text}")
            except Exception as e:
                messagebox.showerror("Грешка", f"Проблем с връзката към сървъра:\n{e}")
            
        
        self.edit_hall_button = Button(self.edit_window, text="Запази промените", width=20, font=("Tahoma", 16), background=SECONDARY_COLOUR, command=submit).pack(pady=20)
             
    def remove_hall(self):
        
        self.window.withdraw()
        self.delete_window = tk.Toplevel(self.window)
        self.delete_window.title("Премахване на зала")
        self.delete_window.geometry("1720x1060")
        self.delete_window.config(bg=MAIN_COLOUR)
        
        self.title_label = Label(self.delete_window, text="Премахване на зала", font=("Tahoma", 26), fg=SECONDARY_COLOUR, background=MAIN_COLOUR)
        self.title_label.pack(pady=35)
        
        def load_rooms():
            try:
                response = requests.get(f"{ROOM_API}/room")
                return response.json()
            except Exception as e:
                messagebox.showerror("Грешка", f"Проблем с връзката към сървъра:\n{e}")
                return []
        
        rooms = load_rooms()
        room_var = tk.StringVar(self.delete_window)
        options = [f"{r['id']}: {r['name']} (капацитет: {r['capacity']})" for r in rooms]
        room_menu = tk.OptionMenu(self.delete_window, room_var, *options)
        room_menu.config(width=50)
        room_menu.pack(pady=20)
        
        def submit():
            selected = room_var.get()
            room_id = int(selected.split(":")[0])
            
            try:
                response = requests.delete(f"{ROOM_API}/rooms/{room_id}")
                if response.status_code == 200:
                    messagebox.showinfo("Успешно", "Зала е премахната успешно.")
                    self.delete_window.destroy()
                    AdminWindow()
                else:
                    messagebox.showerror("Грешка", f"Неуспешно премахване на зала: {response.text}")
            except Exception as e:
                messagebox.showerror("Грешка", f"Проблем с връзката към сървъра:\n{e}")
        
        
        self.delete_hall_button = Button(self.delete_window, text="Премахни", width=20, font=("Tahoma", 16), background=SECONDARY_COLOUR, command=submit)
        self.delete_hall_button.pack(pady=20)

                   
    def load_reservations(self):
        try:
            response = requests.get(f"{RESERVATION_API}/reservations")
            reservations = response.json()
            
            users_response = requests.get(f"{USER_API}/users")
            users_data = users_response.json()
            users = users_data if isinstance(users_data, list) else users_data.get("users", [])
            user_map = {user['id']:user['username'] for user in users}
            
            rooms_respone = requests.get(f"{ROOM_API}/room")
            rooms_data = rooms_respone.json()
            rooms = rooms_data if isinstance(rooms_data, list) else rooms_data.get("rooms", [])
            room_map = {room['id']:room['name'] for room in rooms}
            
        except Exception as e:
            messagebox.showerror("Грешка", f"Проблем с връзката към сървъра:\n{e}")
            return
        
        self.reservations_window = tk.Toplevel(self.window)
        self.reservations_window.title("Всички резервации")
        self.reservations_window.geometry("1720x1060")
        self.reservations_window.config(bg=MAIN_COLOUR)
        
        text = tk.Text(self.reservations_window, wrap=tk.WORD, width=100, height=30, font=("Tahoma", 16), fg=SECONDARY_COLOUR, background=MAIN_COLOUR)
        text.pack(padx=10, pady=10)
        
        for reservation in reservations:
            
            user_name = user_map.get(reservation['user_id'], "Неизвестен потребител")
            room_name = room_map.get(reservation['room_id'], "Неизвестна зала")
            
            text.insert(tk.END, f"Резервация (ID): {reservation['id']}\n")
            text.insert(tk.END, f"Потребител: {reservation['user_id']} ({user_name})\n")
            text.insert(tk.END, f"Зала: {reservation['room_id']} ({room_name})\n")
            text.insert(tk.END, f"Начало на резервация: {reservation['start_time']}\n")
            text.insert(tk.END, f"Край на резервация: {reservation['end_time']}\n\n")
            text.insert(tk.END, "----------------------------------------\n")
        
        
if __name__ == "__main__":
    root = tk.Tk()
    StartWindow(root)
    root.mainloop()
