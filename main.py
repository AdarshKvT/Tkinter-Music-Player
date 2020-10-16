from tkinter import *
from pygame import mixer
import tkinter.messagebox
from tkinter import filedialog



#setting up tkinter window
root = Tk()

mixer.init()

####----------menubar------------###

def open_audio_file():
    global filename
    statusbar['text'] = "Opening File"
    filename = filedialog.askopenfilename()
    statusbar['text'] = "Opened " + filename

def about():
    statusbar['text'] = "About Music Player"
    tkinter.messagebox.showinfo('About Music Player', "Made by Rachit Hooda")

def goodbey():
    statusbar['text'] = "EXIT PLAYER"
    tkinter.messagebox.showinfo('Thankyou', "Thankyou for using Music Player by Rachit Hooda")
    root.destroy()

menubar = Menu(root)
root.config(menu=menubar)

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open Audio", command=open_audio_file)
submenu.add_command(label="Exit Player", command=goodbey)

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About Music Player", command=about)

#-----------------------------------------------------------------#


#basic setup for our window
root.geometry("400x300")
root.resizable(0, 0)

root.title("Music Player by Rachit Hooda")
root.iconbitmap(r"G:\python\Projects\Music Player\assets\music.ico")


###

text = Label(root, text = "Play a song")
text.pack()

##----------MUSIC FUNCTIONS--------------##
def play():
    try:
        paused
    except NameError:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = "Playing Music"
        except:
            statusbar['text'] = "FILE ERROR!!!"
            tkinter.messagebox.showerror('FILE ERROR', "PLEASE SELECT A FILE")
    else:
        mixer.music.unpause()
        statusbar['text'] = "Music Resumed"
        statusbar['text'] = "Playing Music"

play_photo = PhotoImage(file=r"G:\python\Projects\Music Player\assets\video.png")
play_but = Button(root, image = play_photo, command = play)
play_but.pack()

def stop():
    mixer.music.stop()
    statusbar['text'] = "Music Stopped"

stop_photo = PhotoImage(file=r"G:\python\Projects\Music Player\assets\Stop.png")
stop_but = Button(root, image = stop_photo, command = stop)
stop_but.pack()

def pause():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "Music Paused"

pause_photo = PhotoImage(file=r"G:\python\Projects\Music Player\assets\pause.png")
pause_but = Button(root, image = pause_photo, command = pause)
pause_but.pack()

#####


###CONTROLING THE VOLUME###

def vol(value):
    volume = int(value)/100
    mixer.music.set_volume(volume)
    statusbar['text'] = "Change in Volume"


scale = Scale(root,from_=0,to=100, orient=HORIZONTAL, command=vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack()

##########################

statusbar = Label(root, text="Welcome to Music Player by Rachit Hooda", relief=SUNKEN)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
