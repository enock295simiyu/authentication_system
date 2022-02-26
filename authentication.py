import os
import shutil
import webbrowser
from tkinter import Tk, Label, Button, Toplevel, StringVar, Entry, END, Scale, HORIZONTAL, OptionMenu, Scrollbar, \
    VERTICAL, RIGHT, Y, BOTH, Canvas

from database import User
from zoomwindow import ZoomWindow


class Authentication:
    def __init__(self):
        self.path = None
        self.image_render_window = None
        self.logout_screen = None
        self.field = None
        self.scale = None
        self.photo = None
        self.flag_frame_title = None
        self.flag_frame = None
        self.remove_input_button = None
        self.add_input_button = None
        self.input_add_frame = None
        self.scrollbar = None
        self.logout_button = None
        self.download_files_success = None
        self.download_files_title = None
        self.change_color_title = None
        self.chosen_color = None
        self.color_dropdown = None
        self.material_title = None
        self.link5 = None
        self.link4 = None
        self.link3 = None
        self.link2 = None
        self.link1 = None
        self.font_title = None
        self.user_failed_to_login_screen = None
        self.user_logged_in_successfully_screen = None
        self.user_created_successfully_screen = None
        self.user_already_saved_screen = None
        self.password_login_entry = None
        self.username_login_entry = None
        self.password_verify = None
        self.username_verify = None
        self.login_screen = None
        self.registration_screen = None
        self.authentication_window = Tk()
        self.authentication_window.resizable(height=True, width=True)
        self.authentication_window_geometry = '1000x800'
        self.username = None
        self.password = None
        self.password1 = None
        self.username_entry = None
        self.password_entry = None
        self.user = User(self.username, self.password)
        self.color_options = ['white', 'yellow', 'lime', 'aqua', 'azure', 'coral', 'cyan', 'cornflowerblue',
                              'darkorange', 'greenyellow', 'lavenderblush', 'springgreen', 'steelblue']

    def create_base_authentication_window(self):
        self.authentication_window.title('Authentication System | Please Choose between login or register')
        self.authentication_window.geometry(self.authentication_window_geometry)
        Label(text="Choose Login Or Register", bg="blue", fg='white', width="300", height="2",
              font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command=self.login_page).pack()
        Label(text="").pack()
        Button(text="Register", height="2", width="30", command=self.register_page).pack()
        self.scrollbar = Scrollbar(self.authentication_window, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)

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
        Label(self.registration_screen, text="").pack()
        Button(self.registration_screen, text="Register", command=self.register_user, width=10, height=1,
               bg="blue").pack()

    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()
        self.user.username = username_info
        self.user.password = password_info
        user_created, self.user = self.user.save()
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        if not user_created:
            self.user_already_saved()
        else:
            self.user_created_successfully()

        self.registration_screen.destroy()

    def user_already_saved(self):
        self.user_already_saved_screen = Toplevel(self.registration_screen)
        self.user_already_saved_screen.title("The Username you entered is already saved in the database.")
        self.user_already_saved_screen.geometry("800x100")
        Label(self.user_already_saved_screen, text="The Username you entered is already saved in the database. "
                                                   "Please Login or create a new account!").pack()
        Button(self.user_already_saved_screen, text="Login", command=self.login_page).pack()
        Button(self.user_already_saved_screen, text="Register", command=self.register_page).pack()

    def user_created_successfully(self):
        self.user_created_successfully_screen = Toplevel(self.registration_screen)
        self.user_created_successfully_screen.title("The Username account created Successfully.")
        self.user_created_successfully_screen.geometry("800x100")
        Label(self.user_created_successfully_screen, text="The Username account created Successfully. Please Login "
              ).pack()
        Button(self.user_created_successfully_screen, text="Login", command=self.login_page).pack()

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

    def user_logged_in_successfully(self):
        self.user_logged_in_successfully_screen = Toplevel(self.login_screen)
        self.user_logged_in_successfully_screen.title("Login is successful.")
        self.user_logged_in_successfully_screen.geometry("800x100")
        Label(self.user_logged_in_successfully_screen, text="Click the button below to view the main content page"
              ).pack()
        Button(self.user_logged_in_successfully_screen, text="Main Page", ).pack()

    def user_failed_to_login(self):
        self.user_failed_to_login_screen = Toplevel(self.registration_screen)
        self.user_failed_to_login_screen.title("Invalid Credentials.")
        self.user_failed_to_login_screen.geometry("800x100")
        Label(self.user_failed_to_login_screen, text="Either the username you entered or password is incorrect!"
              ).pack()
        Button(self.user_failed_to_login_screen, text="Login", command=self.login_page).pack()

    def login_user(self):
        self.username = self.username_verify.get()
        self.password = self.password_verify.get()
        self.user = User(self.username, self.password)
        user_available = self.user.check_if_user_is_already_saved()
        has_login = False
        if user_available:
            if user_available.get('password') == self.password:
                self.user_logged_in_successfully()
                has_login = True
        if not has_login:
            self.user_failed_to_login()

        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)
        Label(self.login_screen, text="Login was Success", fg="green", font=("calibri", 11)).pack()
        self.login_screen.destroy()
        self.render_main_page()

    def callback(self, url):
        webbrowser.open_new(url)

    def change_font_size(self, val):
        self.font_title.configure(font=('Calibri', val))
        self.link2.configure(font=('Calibri', val))
        self.link1.configure(font=('Calibri', val))
        self.link3.configure(font=('Calibri', val))
        self.link4.configure(font=('Calibri', val))
        self.link5.configure(font=('Calibri', val))
        self.material_title.configure(font=('Calibri', val))
        self.color_dropdown.configure(font=('Calibri', val))
        self.change_color_title.configure(font=('Calibri', val))
        self.download_files_title.configure(font=('Calibri', val))
        self.download_button.configure(font=('Calibri', val))
        self.download_files_success.configure(font=('Calibri', val))
        self.logout_button.configure(font=('Calibri', val))

    def change_background_color(self, color):
        self.authentication_window.configure(bg=color)
        self.link2.configure(bg=color)
        self.link1.configure(bg=color)
        self.link3.configure(bg=color)
        self.link4.configure(bg=color)
        self.link5.configure(bg=color)

    def get_download_path(self):
        """Returns the default downloads path for linux or windows"""
        if os.name == 'nt':
            import winreg
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
            return location
        else:
            return os.path.join(os.path.expanduser('~'), 'downloads')

    def download_file(self):
        try:
            downloads_folder = self.get_download_path()
            shutil.copy2('downloaded_file.txt', downloads_folder)
            self.download_files_success.configure(text='File was downloaded successfully and has been saved to you '
                                                       'downloads folder')
        except:
            self.download_files_success.configure(text='An Error occurred while downloading the file')

    def clear_landing_page(self):
        elements = self.authentication_window.pack_slaves()
        for l in elements:
            l.destroy()

    def render_main_page(self):
        self.clear_landing_page()
        self.authentication_window.title('Main Content')
        self.font_title = Label(text="Change Font Size", bg="blue", fg='white', width="300", height="1",
                                font=("Calibri", 13))
        self.font_title.pack()
        scale = Scale(self.authentication_window, orient=HORIZONTAL, length=300, width=20, sliderlength=10, from_=10,
                      to=50,
                      tickinterval=5, command=self.change_font_size)
        scale.pack()
        self.download_files_title = Label(text="Downloads", bg="blue", fg='white',
                                          width="300", height="1", font=("Calibri", 13))
        self.download_files_title.pack()
        self.download_files_success = Label(bg="yellow", fg='black',
                                            width="300", height="1", font=("Calibri", 13))
        self.download_files_success.pack()
        self.download_button = Button(text="Download File", height="1", width="30", command=self.download_file)
        self.download_button.pack()
        self.material_title = Label(text="List of the best python learning websites", bg="blue", fg='white',
                                    width="300", height="1", font=("Calibri", 13))
        self.material_title.pack()
        self.link1 = Label(self.authentication_window, text="Google", fg="blue", font=("Calibri", 13), cursor="hand2")
        self.link1.pack()
        self.link1.bind("<Button-1>", lambda e: self.callback("https://www.google.com"))
        self.link2 = Label(self.authentication_window, text="Udemy", fg="blue", font=("Calibri", 13), cursor="hand2")
        self.link2.pack()
        self.link2.bind("<Button-1>", lambda e: self.callback("https://www.udemy.com/"))
        self.link3 = Label(self.authentication_window, text="CodeCademy", fg="blue", font=("Calibri", 13),
                           cursor="hand2")
        self.link3.pack()
        self.link3.bind("<Button-1>", lambda e: self.callback("https://www.codecademy.com/"))
        self.link4 = Label(self.authentication_window, text="Educative", fg="blue", font=("Calibri", 13),
                           cursor="hand2")
        self.link4.pack()
        self.link4.bind("<Button-1>", lambda e: self.callback("https://www.educative.io/"))
        self.link5 = Label(self.authentication_window, text="Coursera", fg="blue", font=("Calibri", 13), cursor="hand2")
        self.link5.pack()
        self.link5.bind("<Button-1>", lambda e: self.callback("https://www.coursera.org/"))
        self.change_color_title = Label(text="Change Font Size", bg="blue", fg='white', width="300", height="1",
                                        font=("Calibri", 13))
        self.change_color_title.pack()
        self.chosen_color = StringVar()
        self.chosen_color.set(self.color_options[0])
        self.color_dropdown = OptionMenu(self.authentication_window, self.chosen_color, *self.color_options,
                                         command=self.change_background_color)
        self.color_dropdown.pack()
        self.logout_button = Button(text="Logout", height="1", width="30", command=self.logout_page)
        self.logout_button.pack()
        self.add_input_button = Button(text="Add Input", height="1", width="30", command=self.add_input)
        self.add_input_button.pack()
        self.remove_input_button = Button(text="Remove Input", height="1", width="30", command=self.romove_input)
        self.remove_input_button.pack()
        self.zoom_image_button = Button(text="View Zoom Image", height="2", width="60",
                                          command=self.display_zoom_image)
        self.zoom_image_button.pack()
        self.input_add_frame = Canvas(self.authentication_window)
        self.input_add_frame.pack(fill=BOTH, expand=1)

    def display_zoom_image(self):
        self.path = 'download.png'
        self.image_render_window = Toplevel(self.authentication_window)
        app = ZoomWindow(self.image_render_window, image_path=self.path)

    def add_input(self):
        self.entry = Entry(self.input_add_frame, textvariable=self.username)
        self.entry.pack()

    def romove_input(self):
        for children in self.input_add_frame.pack_slaves():
            children.destroy()

    def logout_page(self):
        self.logout_screen = Toplevel(self.authentication_window)
        self.logout_screen.title("Logout")
        self.logout_screen.geometry(self.authentication_window_geometry)
        Label(self.logout_screen, text="Click the button below to logout").pack()
        Label(self.logout_screen, text="").pack()
        Button(self.logout_screen, text="Logout", width=10, height=1, command=self.logout_user).pack()

    def logout_user(self):

        Label(self.logout_screen, text="Logout was Success", fg="green", font=("calibri", 11)).pack()
        self.logout_screen.destroy()
        self.clear_landing_page()
        self.create_base_authentication_window()
