from modules import *

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue") 
  
sign_up = ctk.CTk() 
sign_up.title("DebtyVibe") 
window_width = 400
window_height = 400
screen_width = sign_up.winfo_screenwidth() 	# ustawianie okna logowania
screen_height = sign_up.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 4
sign_up.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
  
def sign_up_def(): 
  
    username = "1"
    password = "1"
    signin_window = ctk.CTkToplevel(sign_up) 
  
    signin_window.title("New Window") 
  
    signin_window.geometry("350x150") 
  
    user_entry.get()
    user_pass.get()
    if user_entry.get() == username and user_pass.get() == password: 
        sign_up.destroy()
        from sound import root
    elif user_entry.get() == username and user_pass.get() != password: 
        tkmb.showwarning(title='Wrong password',message='Please check your password') 
    elif user_entry.get() != username and user_pass.get() == password: 
        tkmb.showwarning(title='Wrong username',message='Please check your username') 
    else: 
        tkmb.showerror(title="Login Failed",message="Invalid Username and password") 

welcome_label = ctk.CTkLabel(sign_up,text="Witaj w DebtyVibe!") 
welcome_label.pack(pady=20) 
  
login_frame = ctk.CTkFrame(master=sign_up) 
login_frame.pack(pady=20,padx=40,fill='both',expand=True) 
  
signin_label = ctk.CTkLabel(master=login_frame,text='Tutaj stworzysz konto!') 
signin_label.pack(pady=12,padx=10) 
  
user_entry= ctk.CTkEntry(master=login_frame,placeholder_text="Username") 
user_entry.pack(pady=12,padx=10) 
  
user_pass= ctk.CTkEntry(master=login_frame,placeholder_text="Password",show="*") 
user_pass.pack(pady=12,padx=10) 
  
login_btn = ctk.CTkButton(master=login_frame,text='Stwórz konto',command=sign_up_def) 
login_btn.pack(pady=12,padx=10) 
  
sign_up.mainloop()