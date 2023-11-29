from tkinter import *
import customtkinter as ctk 
import tkinter.messagebox as tkmb 
import mysql.connector
from PIL import ImageTk,Image

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue") 
  
root = ctk.CTk()

window_width = 1920
window_height = 1080
screen_width = root.winfo_screenwidth() 	# ustawianie okna logowania
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))


settings_frame = ctk.CTkFrame(master=root, width=100,height=1080, fg_color="#181818", border_color="#161616", border_width=7) 
settings_frame.place(x=0,y=0) 

song_list_frame = ctk.CTkFrame(master=root, width=900,height=650, fg_color="#181818", border_color="#161616", border_width=7) 
song_list_frame.place(x=1020,y=0) 

mixer_frame = ctk.CTkFrame(master=root, width=900,height=600, fg_color="#181818", border_color="#161616", border_width=7) 
mixer_frame.place(x=1020,y=640)

panel_frame = ctk.CTkFrame(master=root, width=600,height=200, fg_color="#202020", border_color="#232323", border_width=7) 
panel_frame.place(x=250,y=700)

ad_frame = ctk.CTkFrame(master=root, width=800,height=600, fg_color="#202020", border_color="#232323", border_width=7)  # reklama
ad_frame.place(x=160,y=50)

settings_label = ctk.CTkLabel(master=root, text="Playlist", fg_color="#181818", text_color="#720404", font=("Impact", 48))
settings_label.place(x=1030,y=5)

logo_image = ctk.CTkImage(Image.open(r"C:\xampp\htdocs\Wydra\Soundplayer\logo.jpg"), size=(90, 90)) # do podmiany zdjecie i sciezka
logo_button = ctk.CTkLabel(master=root, text="", image=logo_image)
logo_button.place(x=10,y=0)

sign_out_image = ctk.CTkImage(Image.open(r"C:\xampp\htdocs\Wydra\Soundplayer\sign_out.png"), size=(100, 100)) # do podmiany zdjecie i sciezka
sign_out_button = ctk.CTkLabel(master=root, text="", image=sign_out_image)
sign_out_button.place(x=0,y=800)

settings_image = ctk.CTkImage(Image.open(r"C:\xampp\htdocs\Wydra\Soundplayer\sett.png"), size=(100, 100)) # do podmiany zdjecie i sciezka
settings_button = ctk.CTkLabel(master=root, text="", image=settings_image)
settings_button.place(x=0,y=900)





root.mainloop()