from tkinter import *
import pyttsx3

engine = pyttsx3.init()


def sRate():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


def male():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)


def female():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)


def speak():
    text_entered = textentry.get()
    engine.say(text_entered)
    engine.runAndWait()


def exit_program():
    window.destroy()
    exit()


window = Tk()

window.configure(background="black")
window.title("Text to Speech Program")
Label(window, text="Enter text", bg="red", fg="white", font="Arial 14 bold").grid(row=0, column=0, sticky=W)
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=1, column=0, sticky=W)
Button(window, text="Play", width=6, command=speak).grid(row=2, column=0, sticky=W)
Label(window, text="Developer:Faheem.k", bg="red", fg="white", font="Arial 12 underline").grid(row=3, column=0, sticky=W)
Label(window, text="Change Gender Voice", bg="red", fg="white", font="Arial 12 underline").grid(row=0, column=3, sticky=E)
Button(window, text="Male", width=6, command=male).grid(row=3, column=2, sticky=E)
Button(window, text="Female", width=6, command=sRate).grid(row=3, column=3, sticky=E)


Button(window, text="Close", width=6, command=exit_program).grid(row=4, column=0, sticky=W)

window.mainloop()