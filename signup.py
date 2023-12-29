from modules import *

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue") 
  
sign_up = ctk.CTk() 
sign_up.iconbitmap('icon.ico')
sign_up.title("DebtyVibe") 
window_width = 400
window_height = 400
screen_width = sign_up.winfo_screenwidth() 	# ustawianie okna logowania
screen_height = sign_up.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 4
sign_up.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
  
def sign_up_def(): 
    us = "user"
    pas = "passwords"

    user_entry.get()
    user_pass.get()
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