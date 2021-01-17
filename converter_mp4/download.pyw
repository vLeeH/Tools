from tkinter import *
import os
win = Tk()
# win.geometry("600x300")
win.resizable(0, 0)
var1 = StringVar()
var2 = IntVar()
Label(win, text="LINK").pack()
e = Entry(win, textvariable=var1)
e.pack(ipadx=160, ipady=5)


def dow(link):
    if var2.get() == 0:
        os.system(f'youtube-dl -o "C:/users/%USERPROFILE%/desktop/" {link}')
        e.delete(0, END)
    elif var2.get() == 1:
        os.system(f'youtube-dl -x --embed-thumbnail -o "C:/users/%USERPROFILE%/desktop/" --audio-format mp3 {link}')
        e.delete(0, END)


Checkbutton(win, text="music", variable=var2).pack()
Button(win, text="DOWNLOAD", command=lambda: dow(var1.get())).pack()
win.mainloop()
