import customtkinter as ctk 
import tkinter.messagebox as tkmb 
import mysql.connector
from tkinter import *
import pygame
from pygame import mixer
import os
import webbrowser
import random
from PIL import ImageTk,Image
import time

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        root.iconbitmap('icon.ico')
        window_width = 1920
        window_height = 1080
        screen_width = root.winfo_screenwidth() 	# ustawianie okna logowania
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()

         # Add these lines
        os.chdir(r"C:\Users\PC\Documents\GitHub\Soundplayer\music")
        self.songtracks = os.listdir()
        self.song_index = 0

        os.chdir(r"C:\Users\PC\Documents\GitHub\Soundplayer\images")
        self.images = os.listdir()


        settings_frame = ctk.CTkFrame(master=root, 
                                    width=100,
                                    height=1080, 
                                    fg_color="#181818", 
                                    border_color="#161616", 
                                    border_width=7)   # ramka ustawien
        settings_frame.place(x=0,y=0) 

        list_frame = ctk.CTkFrame(master=root, 
                                width=820,
                                height=500, 
                                fg_color="#202020", 
                                border_color="#761A06", 
                                border_width=7)   # ramka playlisty
        list_frame.place(x=1060,y=100) 

        mixer_frame = ctk.CTkFrame(master=root, 
                                width=900,
                                height=600, 
                                fg_color="#181818", 
                                border_color="#161616", border_width=7)   # ramka mikseru
        mixer_frame.place(x=1020,y=640)

        fav_song_list_frame = ctk.CTkFrame(master=root, 
                                        width=820,
                                        height=240, 
                                        fg_color="#202020", 
                                        border_color="#761A06", 
                                        border_width=7)   # ramka fav_playlisty
        fav_song_list_frame.place(x=1060,y=730) 

        panel_frame = ctk.CTkFrame(master=root, 
                                width=600,
                                height=200, 
                                fg_color="#202020", 
                                border_color="#232323", 
                                border_width=7) # ramka panelu
        panel_frame.place(x=250,y=700)

        ad_frame = ctk.CTkFrame(master=root, 
                                width=800,
                                height=600, 
                                fg_color="#202020", 
                                border_color="#232323", 
                                border_width=7)  # reklama
        ad_frame.place(x=160,y=50)

        ad_sec_frame = ctk.CTkFrame(master=root, 
                                    width=410,
                                    height=410, 
                                    fg_color="#202020", 
                                    border_color="#761A06",
                                    border_width=7)  # reklama
        ad_sec_frame.place(x=355,y=95)

        trackframe = LabelFrame(self.root, text="Song Track", font=("times new roman", 15, "bold"), bg="#181818", fg="#720404", bd=5, relief=GROOVE)
        trackframe.place(x=250, y=700, width=600, height=70)
        songtrack = Label(trackframe, textvariable=self.track, width=20, font=("times new roman", 18, "bold"), bg="#181818", fg="#720404").grid(row=0, column=1, padx=10, pady=5)
        trackstatus = Label(trackframe, textvariable=self.status, font=("times new roman", 18, "bold"), bg="#181818", fg="#720404").grid(row=0, column=2, padx=10, pady=5)

        play_image = ctk.CTkImage(Image.open(r"..\images\playbtn.png"), 
                          size=(40,40))
        play_btn = ctk.CTkButton(master=root, text="", 
                         image=play_image, 
                         width=30, 
                         height=30, 
                         fg_color="#181818", 
                         command=self.playsong)
        play_btn.place(x=600, y=0)

        prev_image = ctk.CTkImage(Image.open(r"..\images\prevbtn.png"), 
                          size=(40,40))
        prev_btn = ctk.CTkButton(master=root, 
                                text="", 
                                image=prev_image, 
                                width=30, 
                                height=30, 
                                fg_color="#181818", 
                                command=self.prevsong)
        prev_btn.place(x=420, y=780)

        next_image = ctk.CTkImage(Image.open(r"..\images\nextbtn.png"), 
                                size=(40,40))
        next_btn = ctk.CTkButton(master=root, 
                                text="", 
                                image=next_image, 
                                width=30, 
                                height=30, 
                                fg_color="#181818", 
                                command=self.nextsong)
        next_btn.place(x=630, y=780)

        unpause_image = ctk.CTkImage(Image.open(r"..\images\playbtn.png"),
                                     size=(40,40))
        unpause_btn = ctk.CTkButton(master=root, 
                             text="",  
                             image=unpause_image,
                             width=30, 
                             height=30, 
                             fg_color="#181818", 
                             command=self.unpausesong)
        unpause_btn.place(x=490, y=780)
        
        pause_image = ctk.CTkImage(Image.open(r"..\images\pausebtn.png"),
                                   size=(40,40))
        pause_btn = ctk.CTkButton(master=root, 
                           text="",
                           image=pause_image, 
                           width=30, 
                           height=30,  
                           fg_color="#181818",
                           command=self.pausesong) 
        pause_btn.place(x=560, y=780)

        loop_image = ctk.CTkImage(Image.open(r"..\images\loopbtn.png"), 
                          size=(40,40))
        loop_btn = ctk.CTkButton(master=root, 
                                text="", 
                                image=loop_image, 
                                width=30, 
                                height=30, 
                                fg_color="#181818", 
                                command=self.loop_song)
        loop_btn.place(x=730, y=780)

        song_list_frame = ctk.CTkFrame(master=root, 
                                    width=900,
                                    height=650, 
                                    fg_color="#181818", 
                                    border_color="#161616", 
                                    border_width=7)   # ramka playlisty
        song_list_frame.place(x=1020,y=0)
        scrol_y = Scrollbar(song_list_frame, orient=VERTICAL)
        self.playlist = Listbox(song_list_frame, 
                                yscrollcommand=scrol_y.set, 
                                selectbackground="#720404", 
                                selectmode=SINGLE, 
                                font=("times new roman", 16, "bold"), 
                                bg="#181818", 
                                fg="#720404", 
                                bd=5, 
                                relief=GROOVE, 
                                height=22, 
                                width=78)
        scrol_y.place(x=1000, y=100)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.place(x=10, y=70)
        os.chdir(r"C:\Users\PC\Documents\GitHub\Soundplayer\music")
        songtracks = os.listdir()
        for track in songtracks:
            self.playlist.insert(END, track)
        
        logo_image = ctk.CTkImage(Image.open(r"..\images\logo.png"), 
                          size=(90, 90)) # do podmiany zdjecie i sciezka
        logo_button = ctk.CTkLabel(master=root, 
                                text="", 
                                image=logo_image)
        logo_button.place(x=0,y=0)

        sign_out_image = ctk.CTkImage(Image.open(r"..\images\sign_out.png"), 
                                    size=(80, 80)) # do podmiany zdjecie i sciezka
        sign_out_button = ctk.CTkButton(master=root, 
                                        text="", 
                                        image=sign_out_image, 
                                        fg_color="#181818", 
                                        width=80, 
                                        height=80, 
                                        command=self.sign_out)
        sign_out_button.place(x=0,y=840)

        settings_image = ctk.CTkImage(Image.open(r"..\images\sett.png"),
                                    size=(80, 80)) # do podmiany zdjecie i sciezka
        settings_button = ctk.CTkButton(master=root, 
                                        text="", 
                                        image=settings_image, 
                                        fg_color="#181818", 
                                        width=80, 
                                        height=80, 
                                        command=self.settings)
        settings_button.place(x=0,y=920)

        support_image = ctk.CTkImage(Image.open(r"..\images\support.png"),
                                    size=(80, 80)) # do podmiany zdjecie i sciezka
        support_button = ctk.CTkButton(master=root,
                                    text="", 
                                    image=support_image,
                                    fg_color="#181818",
                                    width=80,
                                    height=80,
                                    command=self.support)
        support_button.place(x=0,y=760)

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

        tlo_image = ctk.CTkImage(Image.open(r"..\images\tlo.png"), size=(400,400))   # reklama pingolingo
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
                                    command=self.add)

        click_me_btn.place(x=515,y=400)

        pingolingo_label = ctk.CTkLabel(master=root, 
                                        text="Pingolingo",
                                        font=("Impact", 48),
                                        fg_color=("white"),
                                        text_color=("#720404"),)

        pingolingo_label.place(x=455,y=100)

        vol_image = ctk.CTkImage(Image.open(r"..\images\volbtn.png"))
        vol_label = ctk.CTkLabel(master=root,
                                 text="",
                                 image=vol_image)
        vol_label.place(x=425, y=845)

        self.volume = ctk.DoubleVar(self.root, value=0.5)
        self.volume_scale = ctk.CTkSlider(self.root, 
                               from_=0,
                               to=100, 
                               orientation=HORIZONTAL,
                               button_color="#761A06", 
                               command=self.change_volume)
        self.volume_scale.place(x=450, y=850)

    def change_volume(self, event=None):
        pygame.mixer.music.set_volume(self.volume.get())

    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

        pygame.mixer.music.load(self.songtracks[self.song_index])
        pygame.mixer.music.play()

    def pausesong(self):
        self.status.set("-Paused")
        pygame.mixer.music.pause()

    def unpausesong(self):
        self.status.set("-Playing")
        pygame.mixer.music.unpause()

    def nextsong(self):
        self.song_index += 1
        if self.song_index >= len(self.songtracks):
            self.song_index = 0
        self.playsong()

    def prevsong(self):
        self.song_index -= 1
        if self.song_index < 0:
            self.song_index = len(self.songtracks) - 1
        self.playsong()
    
    def loop_song(self):
        self.status.set("-Looped")
        pygame.mixer.music.play(-1)  # -1 means the song will loop indefinitely
    
    def sign_out(self):  # funkcja wyloguj
        answer = tkmb.askquestion(title='DebtyVibe',message='Czy na pewno chcesz sie wylogować?')
        if answer == "yes":
            root.destroy()
            from signin import sign_in

    def settings(self):  # funkcja ustawienia
        settings_wind = ctk.CTkToplevel()
        settings_wind.geometry('300x300')
        settings_wind.mainloop()

    def support(self):
        url = r'file:///C:\Users\PC\Documents\GitHub\Soundplayer\support.html'
        webbrowser.open_new_tab(url)

    def add(self):  
        url = r'https://github.com/KamaXpl/Pingolingo'
        webbrowser.open_new_tab(url)

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
MusicPlayer(root)
root.mainloop()
