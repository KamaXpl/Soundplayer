import customtkinter as ctk 
import tkinter.messagebox as tkmb 
import mysql.connector


  
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue") 
  
app = ctk.CTk() 
app.title("DebtyVibe") 
window_width = 500
window_height = 500
screen_width = app.winfo_screenwidth() 	# ustawianie okna logowania
screen_height = app.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 4
app.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
  
  
def login(): 
  
    username = "Izabela"
    password = "Izzy"
    signin_window = ctk.CTkToplevel(app) 
  
    signin_window.title("New Window") 
  
    signin_window.geometry("350x150") 
  
    if user_entry.get() == username and user_pass.get() == password: 
        tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
        signin_window.destroy()
    elif user_entry.get() == username and user_pass.get() != password: 
        tkmb.showwarning(title='Wrong password',message='Please check your password') 
    elif user_entry.get() != username and user_pass.get() == password: 
        tkmb.showwarning(title='Wrong username',message='Please check your username') 
    else: 
        tkmb.showerror(title="Login Failed",message="Invalid Username and password") 


def create_account():

    signup_window = ctk.CTkToplevel(app)

    signup_window.title("Tworzenie konta")

    signup_window.geometry("350x150")


welcome_label = ctk.CTkLabel(app,text="Witaj w DebtyVibe!") 
welcome_label.pack(pady=20) 
  
login_frame = ctk.CTkFrame(master=app) 
login_frame.pack(pady=20,padx=40,fill='both',expand=True) 
  
signin_label = ctk.CTkLabel(master=login_frame,text='Zaloguj się!') 
signin_label.pack(pady=12,padx=10) 
  
  
user_entry= ctk.CTkEntry(master=login_frame,placeholder_text="Username") 
user_entry.pack(pady=12,padx=10) 
  
user_pass= ctk.CTkEntry(master=login_frame,placeholder_text="Password",show="*") 
user_pass.pack(pady=12,padx=10) 
  
  
login_btn = ctk.CTkButton(master=login_frame,text='Login',command=login) 
login_btn.pack(pady=12,padx=10) 
  
remember_me = ctk.CTkCheckBox(master=login_frame,text='Remember Me') 
remember_me.pack(pady=12,padx=10) 

label2 = ctk.CTkLabel(master=login_frame, text="Nie masz konta?")
label2.pack(pady=12,padx=10)

btn_signup = ctk.CTkButton(master=login_frame, text="Stwórz je tutaj!", command=create_account)
btn_signup.pack(pady=12, padx=10)
  
app.mainloop()