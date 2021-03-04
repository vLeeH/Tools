from tkinter import *
import pytube
from pytube import YouTube
# github.com/vLeeH - 2021

# Functions
def download(): 
    """The function to download the youtube video."""
    video_url = url.get()
    try: 
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first() # First stream avaible
        video.download('C:/Users/User/Desktop/Vídeos')
        notif.config(fg='green', text='Download complete.')

    except Exception as e: 
        print(f'[ERROR]{e}')
        notif.config(fg='red', text='Video could not be downloaded')



# Interface using Tkinter
# Screen 
master = Tk()
master.title('Youtube Video Downloader')

# Labels 
Label(master, text='Youtube Video Converter', fg="red", font=("Arial", 15)).grid(sticky=N, padx=100, row=0)
Label(master, text='Enter the link to your video below: ', font=("Arial", 12)).grid(sticky=N, row=1, pady=15)
notif = Label(master, font=('Calibri', 12))
notif.grid(sticky=N, pady=1, row=4)

# Vars 
url = StringVar()

# Entry
Entry(master, width=50).grid(sticky=N, row=2)

# Button 
Button(master, width=20, text='Download', font=('Calibri',12), command=download).grid(sticky=N, row=3, pady=15)

master.mainloop()
