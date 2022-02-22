from tkinter import Tk, Label, Button, Toplevel, StringVar, Entry, END


class Authentication:
    def __init__(self):
        self.password_login_entry = None
        self.username_login_entry = None
        self.password_verify = None
        self.username_verify = None
        self.login_screen = None
        self.registration_screen = None
        self.authentication_window = Tk()
        self.authentication_window_geometry = '800x600'
        self.username = None
        self.password = None
        self.password1 = None
        self.username_entry = None
        self.password_entry = None

    def create_base_authentication_window(self):
        self.authentication_window.title('Authentication System | Please Choose between login or register')
        self.authentication_window.geometry(self.authentication_window_geometry)
        Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command=self.login_page).pack()
        Label(text="").pack()
        Button(text="Register", height="2", width="30", command=self.register_page).pack()

    def register_page(self):
        self.registration_screen = Toplevel(self.authentication_window)
        self.registration_screen.title("Authentication System | Register")
        self.registration_screen.geometry(self.authentication_window_geometry)
        self.username = StringVar()
        self.password = StringVar()
        self.password1 = StringVar()
        Label(self.registration_screen, text="Please enter details below", bg="blue").pack()
        Label(self.registration_screen, text="").pack()
        username_label = Label(self.registration_screen, text="Username * ")
        username_label.pack()
        self.username_entry = Entry(self.registration_screen, textvariable=self.username)
        self.username_entry.pack()
        password_label = Label(self.registration_screen, text="Password * ")
        password_label.pack()
        self.password_entry = Entry(self.registration_screen, textvariable=self.password, show='*')
        self.password_entry.pack()
        password1_label = Label(self.registration_screen, text="Re-Password *")
        password1_label.pack()
        password1_entry = Entry(self.registration_screen, textvariable=self.password1, show='*')
        password1_entry.pack()
        Label(self.registration_screen, text="").pack()
        Button(self.registration_screen, text="Register", command=self.register_user, width=10, height=1,
               bg="blue").pack()

    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()
        password_info1 = self.password1.get()
        if password_info1 != password_info:
            pass

        # Open file in write mode
        file = open(username_info, "w")

        # write username and password information into file
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()

        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        # set a label for showing success information on screen

        Label(self.registration_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

    def login_page(self):
        self.login_screen = Toplevel(self.authentication_window)
        self.login_screen.title("Login")
        self.login_screen.geometry(self.authentication_window_geometry)
        Label(self.login_screen, text="Please enter details below to login").pack()
        Label(self.login_screen, text="").pack()
        self.username_verify = StringVar()
        self.password_verify = StringVar()

        Label(self.login_screen, text="Username * ").pack()
        self.username_login_entry = Entry(self.login_screen, textvariable=self.username_verify)
        self.username_login_entry.pack()
        Label(self.login_screen, text="").pack()
        Label(self.login_screen, text="Password * ").pack()
        self.password_login_entry = Entry(self.login_screen, textvariable=self.password_verify, show='*')
        self.password_login_entry.pack()
        Label(self.login_screen, text="").pack()
        Button(self.login_screen, text="Login", width=10, height=1, command=self.login_user).pack()

    def login_user(self):
        self.username = self.username_verify.get()
        self.password = self.password_verify.get()
        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)
        Label(self.login_screen, text="Login was Success", fg="green", font=("calibri", 11)).pack()
        self.login_screen.destroy()
