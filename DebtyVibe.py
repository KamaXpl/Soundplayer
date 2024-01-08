from modules import *
from PIL import ImageTk,Image

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
                                    width=510,
                                    height=510, 
                                    fg_color="#202020", 
                                    border_color="#761A06",
                                    border_width=10)  # reklama
        ad_sec_frame.place(x=315,y=95)

        trackframe = LabelFrame(self.root, text="Song Track", font=("times new roman", 15, "bold"), bg="#181818", fg="#720404", bd=5, relief=GROOVE)
        trackframe.place(x=250, y=700, width=600, height=70)
        songtrack = Label(trackframe, textvariable=self.track, width=20, font=("times new roman", 18, "bold"), bg="#181818", fg="#720404").grid(row=0, column=1, padx=10, pady=5)
        trackstatus = Label(trackframe, textvariable=self.status, font=("times new roman", 18, "bold"), bg="#181818", fg="#720404").grid(row=0, column=2, padx=10, pady=5)

        prev_image = ctk.CTkImage(Image.open(r"..\images\prevbtn.png"), 
                          size=(40,40))
        prev_btn = ctk.CTkButton(master=root, 
                                text="", 
                                image=prev_image, 
                                width=30, 
                                height=30, 
                                fg_color="#181818", 
                                command=self.prevsong)
        prev_btn.place(x=460, y=780)

        next_image = ctk.CTkImage(Image.open(r"..\images\nextbtn.png"), 
                                size=(40,40))
        next_btn = ctk.CTkButton(master=root, 
                                text="", 
                                image=next_image, 
                                width=30, 
                                height=30, 
                                fg_color="#181818", 
                                command=self.nextsong)
        next_btn.place(x=590, y=780)

        pause_image = ctk.CTkImage(Image.open(r"..\images\pausebtn.png"),
                                     size=(40,40))
        
        unpause_image = ctk.CTkImage(Image.open(r"..\images\playbtn.png"),
                                     size=(40,40))
        
        pauseplay_btn = ctk.CTkButton(master=root, 
                             text="",  
                             image=unpause_image,
                             width=30, 
                             height=30, 
                             fg_color="#181818", 
                             command=self.pauseplay)
        pauseplay_btn.place(x=525, y=780)
        
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

        fav_image = ctk.CTkImage(Image.open(r"..\images\favbtn.png"), 
                          size=(40,40))
        fav_btn = ctk.CTkButton(master=root, 
                                text="", 
                                image=fav_image, 
                                width=30, 
                                height=30, 
                                fg_color="#181818", 
                                command=self.loop_song)
        fav_btn.place(x=320, y=780)

        song_list_frame = ctk.CTkFrame(master=root, 
                                    width=900,
                                    height=650, 
                                    fg_color="#181818", 
                                    border_color="#161616", 
                                    border_width=7)   
        song_list_frame.place(x=1020,y=0)

        scrol_y = Scrollbar(song_list_frame, orient=VERTICAL)
        self.playlist = Listbox(song_list_frame, 
                                yscrollcommand=scrol_y.set, 
                                selectbackground="#720404", 
                                selectmode=SINGLE, 
                                font=("times new roman", 16, "bold"), 
                                bg="#181818", 
                                fg="#BA0404", 
                                bd=5, 
                                relief=GROOVE, 
                                height=22, 
                                width=78)
        scrol_y.place(x=1000, y=100)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.place(x=10, y=70)

        scrol_z = Scrollbar(fav_song_list_frame, orient=VERTICAL)
        self.favplaylist = Listbox(fav_song_list_frame, 
                                yscrollcommand=scrol_z.set, 
                                selectbackground="#720404", 
                                selectmode=SINGLE, 
                                font=("times new roman", 16, "bold"), 
                                bg="#181818", 
                                fg="#720404", 
                                bd=5, 
                                relief=GROOVE, 
                                height=9, 
                                width=73)
        scrol_z.place(x=100, y=500)
        scrol_z.config(command=self.favplaylist.yview)
        self.favplaylist.place(x=3, y=1)

        os.chdir(r"C:\Users\PC\Documents\GitHub\Soundplayer\music")
        songtracks = os.listdir()
        for track in songtracks:
            self.playlist.insert(END, track)
        
        logo_image = ctk.CTkImage(Image.open(r"..\images\logo.png"), 
                          size=(80, 80)) 
        logo_button = ctk.CTkLabel(master=root, 
                                text="", 
                                image=logo_image)
        logo_button.place(x=10,y=0)

        sign_out_image = ctk.CTkImage(Image.open(r"..\images\sign_out.png"), 
                                    size=(80, 80)) 
        sign_out_button = ctk.CTkButton(master=root, 
                                        text="", 
                                        image=sign_out_image, 
                                        fg_color="#181818", 
                                        width=80, 
                                        height=80, 
                                        command=self.sign_out)
        sign_out_button.place(x=0,y=840)

        settings_image = ctk.CTkImage(Image.open(r"..\images\sett.png"),
                                    size=(80, 80)) 
        settings_button = ctk.CTkButton(master=root, 
                                        text="", 
                                        image=settings_image, 
                                        fg_color="#181818", 
                                        width=80, 
                                        height=80, 
                                        command=self.settings)
        settings_button.place(x=0,y=920)

        support_image = ctk.CTkImage(Image.open(r"..\images\support.png"),
                                    size=(80, 80))
        support_button = ctk.CTkButton(master=root,
                                    text="", 
                                    image=support_image,
                                    fg_color="#181818",
                                    width=80,
                                    height=80,
                                    command=self.support)
        support_button.place(x=0,y=760)

        premium_image = ctk.CTkImage(Image.open(r"..\images\premium.png"),
                                    size=(80, 80)) 
        premium_button = ctk.CTkButton(master=root,
                                    text="", 
                                    image=premium_image,
                                    fg_color="#181818",
                                    width=80,
                                    height=80,
                                    command=self.premium)
        premium_button.place(x=0,y=80)

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

        tlo_image = ctk.CTkImage(Image.open(r"..\images\tlo.png"), size=(500,500))   # reklama pingolingo
        tlo_btn = ctk.CTkLabel(master=root, 
                            text="", 
                            image=tlo_image, 
                            width=30, 
                            height=30, 
                            fg_color="#181818")

        tlo_btn.place(x=320,y=100)

        play_image = ctk.CTkImage(Image.open(r"..\images\playlistbtn.png"), 
                          size=(40,40))
        play_btn = ctk.CTkButton(master=root, text="", 
                         image=play_image, 
                         width=30, 
                         height=30, 
                         fg_color="#181818", 
                         command=self.playsong)
        play_btn.place(x=1200, y=10)

        favplay_image = ctk.CTkImage(Image.open(r"..\images\playlistbtn.png"), 
                          size=(40,40))
        favplay_btn = ctk.CTkButton(master=root, text="", 
                         image=play_image, 
                         width=30, 
                         height=30, 
                         fg_color="#181818", 
                         command=self.playsong)
        favplay_btn.place(x=1200, y=67500)

        click_me_btn = ctk.CTkButton(master=root,
                                    text="Click me",
                                    width=200,
                                    height=120,
                                    font=("Impact", 40),
                                    fg_color=("white"),
                                    text_color=("#720404"),
                                    border_color=("white"),
                                    command=self.add)

        click_me_btn.place(x=460,y=450)

        pingolingo_label = ctk.CTkLabel(master=root, 
                                        text="Pingolingo",
                                        font=("Impact", 48),
                                        fg_color=("white"),
                                        text_color=("#BA0404"),)

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
                               button_color="#BA0404", 
                               command=self.change_volume)
        self.volume_scale.place(x=450, y=850)

        add_song_button = ctk.CTkButton(self.root,
                                         text="Add Song",
                                           command=self.add_song_to_playlist,
                                             bg_color="#720404",
                                               fg_color="#720404",
                                                 hover_color="#720404")
        add_song_button.place(x=1725, y=25)

        soon = ctk.CTkLabel(master=root,
                            text="Już niedługo!",
                            fg_color="#181818", 
                            text_color="#BA0404", 
                            font=("Impact", 48))
        
        soon.place(x=1350,y=820)


    def add_song_to_playlist(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("MP3 files", "*.mp3")])
        if file_paths:
            for path in file_paths:
                self.playlist.insert(END, path.split("/")[-1])
                print(f"Added songs to playlist: {file_paths}")

    def change_volume(self, event=None):
        pygame.mixer.music.set_volume(self.volume.get())

    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

        pygame.mixer.music.load(self.songtracks[self.song_index])
        pygame.mixer.music.play()

    def pauseplay(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.status.set("-Paused")
        else:
            pygame.mixer.music.unpause()
            self.status.set("-Playing")

    def nextsong(self):
        self.song_index += 1
        if self.song_index >= len(self.songtracks):
            self.song_index = 0
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        self.playsong()

    def prevsong(self):
        self.song_index -= 1
        if self.song_index < 0:
            self.song_index = len(self.songtracks) - 1
        self.playsong()
    
    def loop_song(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)
            self.status.set("-Looped")
        else:
            pygame.mixer.music.play(1)
            self.status.set("-Playing")

        self.update_track_label()
    
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

    def premium(self):
        url = r'file:///C:\Users\PC\Documents\GitHub\Soundplayer\premium.html'
        webbrowser.open_new_tab(url)

    def add(self):  
        url = r'https://github.com/KamaXpl/Pingolingo'
        webbrowser.open_new_tab(url)

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
MusicPlayer(root)
root.mainloop()
