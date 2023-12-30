from modules import *
import mysql.connector

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

sign_up = ctk.CTk()
sign_up.iconbitmap('icon.ico')
sign_up.title("DebtyVibe")
window_width = 400
window_height = 400
screen_width = sign_up.winfo_screenwidth()
screen_height = sign_up.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 4
sign_up.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# Function to sign up the user
def sign_up_def():
    # Get username and password from entry widgets
    username = user_entry.get()
    password = user_pass.get()

    if len(user_entry.get()) >= 3 and len(user_pass.get()) >= 7: 
        tkmb.showinfo(title="DebtyVibe", message="Utworzono konto! \n Teraz możesz sie zalogować do DebtyVibe!")
        sign_up.destroy()
        from signin import sign_in
    elif len(user_entry.get()) >= 3 and str(user_pass.get()) != 7: 
        tkmb.showwarning(title='DebtyVibe',message='Niepoprawne hasło!') 
    elif len(user_entry.get()) != 3 and len(user_pass.get()) >= 7: 
        tkmb.showwarning(title='DebtyVibe',message='Niepoprawna nazwa!') 
    else: 
        tkmb.showerror(title="DebtyVibe",message="Niepoprawna nazwa i hasło!") 
    
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="debtyvibe_database"
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Check if the username already exists
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        tkmb.showwarning(title='DebtyVibe', message='Username already exists!')
    else:
        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        tkmb.showinfo(title="DebtyVibe", message="Account created successfully! You can now log in to DebtyVibe.")
        sign_up.destroy()
        from signin import sign_in

    # Close the database connection
    cursor.close()
    db.close()

welcome_label = ctk.CTkLabel(sign_up, text="Welcome to DebtyVibe!")
welcome_label.pack(pady=20)

login_frame = ctk.CTkFrame(master=sign_up)
login_frame.pack(pady=20, padx=40, fill='both', expand=True)

signin_label = ctk.CTkLabel(master=login_frame, text='Create your account here!')
signin_label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=login_frame, placeholder_text="Password", show="*")
user_pass.pack(pady=12, padx=10)

login_btn = ctk.CTkButton(master=login_frame, text='Create Account', command=sign_up_def)
login_btn.pack(pady=12, padx=10)

sign_up.mainloop()
