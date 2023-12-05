from modules import *
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

def sign_out(): # funkcja wyloguj
    answer = tkmb.askquestion(title='DebtyVibe',message='Czy na pewno chcesz sie wylogować?')
    if answer == "yes":
        root.destroy()
        from signin import sign_in

def settings(): # funkcja ustawienia
    settings_wind = ctk.CTkToplevel()
    settings_wind.geometry('300x300')
    settings_wind.mainloop()

settings_frame = ctk.CTkFrame(master=root, width=100,height=1080, fg_color="#181818", border_color="#161616", border_width=7)   # ramka ustawien
settings_frame.place(x=0,y=0) 

song_list_frame = ctk.CTkFrame(master=root, width=900,height=650, fg_color="#181818", border_color="#161616", border_width=7)   # ramka playlisty
song_list_frame.place(x=1020,y=0) 

mixer_frame = ctk.CTkFrame(master=root, width=900,height=600, fg_color="#181818", border_color="#161616", border_width=7)   # ramka mikseru
mixer_frame.place(x=1020,y=640)

panel_frame = ctk.CTkFrame(master=root, width=600,height=200, fg_color="#202020", border_color="#232323", border_width=7) # ramka panelu
panel_frame.place(x=250,y=700)

ad_frame = ctk.CTkFrame(master=root, width=800,height=600, fg_color="#202020", border_color="#232323", border_width=7)  # reklama
ad_frame.place(x=160,y=50)

def volumechanger():
    pygame.mixer.music.set_volume(volume_changer.get())

def play():
    pygame.mixer.music.load('background.wav')
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

volume_changer = ctk.CTkSlider(root, from_=0, to=100, command=volumechanger)
volume_changer.place(x=450, y=870)

play_image = ctk.CTkImage(Image.open("playbtn.png"), size=(30,30))
play_btn = ctk.CTkButton(master=root, text="", image=play_image, width=30, height=30, fg_color="#181818", command=play)
play_btn.place(x=400, y=800)

pause_image = ctk.CTkImage(Image.open("playbtn.png"), size=(30,30))
pause_btn = ctk.CTkButton(master=root, text="", image=play_image, width=30, height=30, fg_color="#181818", command=pause)
pause_btn.place(x=450, y=800)

unpause_image = ctk.CTkImage(Image.open("playbtn.png"), size=(30,30))
unpause_btn = ctk.CTkButton(master=root, text="", image=play_image, width=30, height=30, fg_color="#181818", command=unpause)
unpause_btn.place(x=500, y=800)

playlist_label = ctk.CTkLabel(master=root, text="Playlist", fg_color="#181818", text_color="#720404", font=("Impact", 48))
playlist_label.place(x=1030,y=5)

logo_image = ctk.CTkImage(Image.open("logo.jpg"), size=(90, 90)) # do podmiany zdjecie i sciezka
logo_button = ctk.CTkLabel(master=root, text="", image=logo_image)
logo_button.place(x=0,y=0)

sign_out_image = ctk.CTkImage(Image.open("sign_out.png"), size=(80, 80)) # do podmiany zdjecie i sciezka
sign_out_button = ctk.CTkButton(master=root, text="", image=sign_out_image, fg_color="#181818", width=80, height=80, command=sign_out)
sign_out_button.place(x=0,y=840)

settings_image = ctk.CTkImage(Image.open("sett.png"), size=(80, 80)) # do podmiany zdjecie i sciezka
settings_button = ctk.CTkButton(master=root, text="", image=settings_image, fg_color="#181818", width=80, height=80, command=settings)
settings_button.place(x=0,y=920)

root.mainloop()