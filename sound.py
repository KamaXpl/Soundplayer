from modules import *
from PIL import ImageTk,Image

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue") 
  
root = ctk.CTk()
root.iconbitmap('icon.ico')

window_width = 1920
window_height = 1080
screen_width = root.winfo_screenwidth() 	# ustawianie okna logowania
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

def sign_out():  # funkcja wyloguj
    answer = tkmb.askquestion(title='DebtyVibe',message='Czy na pewno chcesz sie wylogować?')
    if answer == "yes":
        root.destroy()
        from signin import sign_in

def settings():  # funkcja ustawienia
    settings_wind = ctk.CTkToplevel()
    settings_wind.geometry('300x300')
    settings_wind.mainloop()

def support():
    url = r'file:///C:\Users\PC\Documents\GitHub\Soundplayer\support.html'
    webbrowser.open_new_tab(url)

def add():  
    url = r'https://github.com/KamaXpl/Pingolingo'
    webbrowser.open_new_tab(url)

settings_frame = ctk.CTkFrame(master=root, width=100,height=1080, fg_color="#181818", border_color="#161616", border_width=7)   # ramka ustawien
settings_frame.place(x=0,y=0) 

song_list_frame = ctk.CTkFrame(master=root, width=900,height=650, fg_color="#181818", border_color="#161616", border_width=7)   # ramka playlisty
song_list_frame.place(x=1020,y=0) 

list_frame = ctk.CTkFrame(master=root, width=820,height=500, fg_color="#202020", border_color="#761A06", border_width=7)   # ramka playlisty
list_frame.place(x=1060,y=100) 

mixer_frame = ctk.CTkFrame(master=root, width=900,height=600, fg_color="#181818", border_color="#161616", border_width=7)   # ramka mikseru
mixer_frame.place(x=1020,y=640)

fav_song_list_frame = ctk.CTkFrame(master=root, width=820,height=320, fg_color="#202020", border_color="#761A06", border_width=7)   # ramka fav_playlisty
fav_song_list_frame.place(x=1060,y=730) 

panel_frame = ctk.CTkFrame(master=root, width=600,height=200, fg_color="#202020", border_color="#232323", border_width=7) # ramka panelu
panel_frame.place(x=250,y=700)

ad_frame = ctk.CTkFrame(master=root, width=800,height=600, fg_color="#202020", border_color="#232323", border_width=7)  # reklama
ad_frame.place(x=160,y=50)

ad_sec_frame = ctk.CTkFrame(master=root, width=410,height=410, fg_color="#202020", border_color="#761A06", border_width=7)  # reklama
ad_sec_frame.place(x=355,y=95)

def volumechanger():
    pygame.mixer.music.set_volume(volume_changer.get())

def play():
    pygame.mixer.music.load('background.wav')
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

volume_changer = ctk.CTkSlider(root, from_=0, to=100, button_color="#761A06", command=volumechanger)
volume_changer.place(x=450, y=850)

play_image = ctk.CTkImage(Image.open("playbtn.png"), size=(40,40))
play_btn = ctk.CTkButton(master=root, text="", image=play_image, width=30, height=30, fg_color="#181818", command=play)
play_btn.place(x=492, y=780)

prev_image = ctk.CTkImage(Image.open("prevbtn.png"), size=(40,40))
prev_btn = ctk.CTkButton(master=root, text="", image=prev_image, width=30, height=30, fg_color="#181818", command=pause)
prev_btn.place(x=432, y=780)

next_image = ctk.CTkImage(Image.open("nextbtn.png"), size=(40,40))
next_btn = ctk.CTkButton(master=root, text="", image=next_image, width=30, height=30, fg_color="#181818", command=unpause)
next_btn.place(x=552, y=780)

loop_image = ctk.CTkImage(Image.open("loopbtn.png"), size=(40,40))
loop_btn = ctk.CTkButton(master=root, text="", image=loop_image, width=30, height=30, fg_color="#181818", command=unpause)
loop_btn.place(x=612, y=780)

logo_image = ctk.CTkImage(Image.open("logo.png"), size=(90, 90)) # do podmiany zdjecie i sciezka
logo_button = ctk.CTkLabel(master=root, text="", image=logo_image)
logo_button.place(x=0,y=0)

sign_out_image = ctk.CTkImage(Image.open("sign_out.png"), size=(80, 80)) # do podmiany zdjecie i sciezka
sign_out_button = ctk.CTkButton(master=root, text="", image=sign_out_image, fg_color="#181818", width=80, height=80, command=sign_out)
sign_out_button.place(x=0,y=840)

settings_image = ctk.CTkImage(Image.open("sett.png"), size=(80, 80)) # do podmiany zdjecie i sciezka
settings_button = ctk.CTkButton(master=root, text="", image=settings_image, fg_color="#181818", width=80, height=80, command=settings)
settings_button.place(x=0,y=920)

support_image = ctk.CTkImage(Image.open("support.png"), size=(80, 80)) # do podmiany zdjecie i sciezka
support_button = ctk.CTkButton(master=root, text="", image=support_image, fg_color="#181818", width=80, height=80, command=support)
support_button.place(x=0,y=760)




# LABEL

playlist_label = ctk.CTkLabel(master=root, 
                              text="Playlist", 
                              fg_color="#181818", 
                              text_color="#720404", 
                              font=("Impact", 48))

playlist_label.place(x=1030,y=5)


fav_song_label = ctk.CTkLabel(master=root, 
                              text="Favorite songs", 
                              fg_color="#181818", 
                              text_color="#720404", 
                              font=("Impact", 48))

fav_song_label.place(x=1030,y=650)

# REKLAMA

tlo_image = ctk.CTkImage(Image.open("tlo.png"), size=(400,400))   # reklama pingolingo
tlo_btn = ctk.CTkLabel(master=root, 
                       text="", 
                       image=tlo_image, 
                       width=30, 
                       height=30, 
                       fg_color="#181818")

tlo_btn.place(x=360,y=100)


click_me_btn = ctk.CTkButton(master=root,
                               text="Click me",
                               width=100,
                               height=60,
                               font=("Impact", 20),
                               fg_color=("white"),
                               text_color=("#720404"),
                               border_color=("white"),
                               command=add)

click_me_btn.place(x=515,y=400)

pingolingo_label = ctk.CTkLabel(master=root, 
                                text="Pingolingo",
                                font=("Impact", 48),
                                fg_color=("white"),
                                text_color=("#720404"),)

pingolingo_label.place(x=455,y=100)

root.mainloop()