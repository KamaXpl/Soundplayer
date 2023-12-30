from modules import *
from PIL import ImageTk,Image
import subprocess  # Import the subprocess module for opening another script
import sys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

sign_in = ctk.CTk()
sign_in.iconbitmap('icon.ico')
sign_in.title("DebtyVibe")
window_width = 500
window_height = 500
screen_width = sign_in.winfo_screenwidth()
screen_height = sign_in.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 4
sign_in.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

def sign_in_def():
    # Get username and password from entry widgets
    username = user_entry.get()
    password = user_pass.get()

    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="debtyvibe_database"
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Check if the username and password match a record in the database
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    if user:
        tkmb.showinfo(title="DebtyVibe", message="Login successful!")
        sign_in.destroy()
        from sound import root
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username and password")

    # Close the database connection
    cursor.close()
    db.close()

def create_account():
    sign_in.destroy()
    from signup import sign_up

welcome_label = ctk.CTkLabel(sign_in, text="Witaj w DebtyVibe!")
welcome_label.pack(pady=20)

login_frame = ctk.CTkFrame(master=sign_in)
login_frame.pack(pady=20, padx=40, fill='both', expand=True)

signin_label = ctk.CTkLabel(master=login_frame, text='Zaloguj się!')
signin_label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=login_frame, placeholder_text="Password", show="*")
user_pass.pack(pady=12, padx=10)

login_btn = ctk.CTkButton(master=login_frame, text='Login', command=sign_in_def)
login_btn.pack(pady=12, padx=10)

remember_me = ctk.CTkCheckBox(master=login_frame, text='Remember Me')
remember_me.pack(pady=12, padx=10)

label2 = ctk.CTkLabel(master=login_frame, text="Nie masz konta?")
label2.pack(pady=12, padx=10)

btn_signup = ctk.CTkButton(master=login_frame, text="Stwórz je tutaj!", command=create_account)
btn_signup.pack(pady=12, padx=10)

sign_in.mainloop()