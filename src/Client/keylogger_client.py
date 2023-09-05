import tkinter as tk
from tkinter import Text, Button
from tkinter import *
from PIL import ImageTk, Image
BUFSIZ = 1024 * 4

import os
import sys
def path(file_name):
    file_name = 'pic\\' + file_name
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, file_name)

def hook(client, button):
    client.sendall(bytes("HOOK", "utf8"))
    if button['text'] == "Hook":
        button.configure(text = "Unhook")
    else:
        button.configure(text = "Hook")
    return
    
def _print(client, textbox):
    client.sendall(bytes("PRINT", "utf8"))
    print("  ")
    data = client.recv(BUFSIZ).decode("utf8")
    data = data[1:]
    textbox.config(state = "normal")
    textbox.insert(tk.END, data)
    textbox.config(state = "disable")
    return
        
def delete(textbox):
    textbox.config(state = "normal")
    textbox.delete("1.0", "end")
    textbox.config(state = "disable")
    return

def lock(client, button):
    client.sendall(bytes("LOCK", "utf8"))
    if button['text'] == "Lock":
        button.configure(text = "Unlock")
    else:
        button.configure(text = "Lock")
    return

def back():
    return

class Keylogger_UI(Frame):
    def __init__(self, parent,client):    
        Frame.__init__(self, parent)
        self.configure(
            bg = "#ff0000",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        parent.geometry("1000x600+200+200")
        self.grid(row=0, column=0, sticky="nsew")

        #frame design
        # self.frame_image = ImageTk.PhotoImage(Image.open(path("bg6.png")))
        self.frame_image = ImageTk.PhotoImage(Image.open(r"src\Client\pic\mmt.jpg"))

        # goi label de pritn cai icon nay len do
        self.frame_image_label = Label(self, image=self.frame_image, bg='black')
        self.frame_image_label.place(x=0, y=0)

        self.text_1 = Text(
            self, height = 200, width = 500, state = "disable", wrap = "char",
            bd=0,
            bg='white',
            highlightthickness=0
        )
        self.text_1.place(
            x=220,
            y=100,
            width=600,
            height=360
        )

        self.button_hook = Button(self, text = 'Hook', width = 20, height = 5, fg = '#ffffff', bg = '#783497',
            borderwidth=0,
            highlightthickness=0,
            font='Helvetica 15 bold',
            command=lambda: hook(client, self.button_hook),
            relief="raised"
        )

        self.button_hook.place(
            x=850,
            y=150,
            width=135,
            height=53.0
        )

        self.button_lock = Button(self, text = 'Lock', width = 20, height = 5, fg = '#ffffff', bg = '#783497',
            borderwidth=0,
            highlightthickness=0,
            font='Helvetica 15 bold',
            command=lambda: lock(client, self.button_lock),
            relief="raised"
        )

        self.button_lock.place(
            x=850,
            y=300,
            width=135,
            height=53
        )

        self.button_print = Button(self, text = 'Show', width = 20, height = 5, fg = '#ffffff', bg = '#783497',
            borderwidth=0,
            highlightthickness=0,
            font='Helvetica 15 bold',
            command=lambda: _print(client, self.text_1),
            relief="raised"
        )

        self.button_print.place(
            x=30,
            y=150,
            width=135,
            height=53
        )

        self.button_delete = Button(self, text = 'Delete', width = 20, height = 5, fg = '#ffffff', bg = '#783497',
            borderwidth=0,
            highlightthickness=0,
            font='Helvetica 15 bold',
            command=lambda: delete(self.text_1),
            relief="raised"
        )

        self.button_delete.place(
            x=30,
            y=300,
            width=135,
            height=53.0
        )

        self.button_back = Button(self, text = 'BACK', width = 20, height = 5, fg = '#ffffff', bg = '#783497',
            borderwidth=0,
            highlightthickness=0,
            font='Helvetica 15 bold',
            command= back,
            relief="raised"
        )

        self.button_back.place(
            x=500,
            y=520,
            width=135,
            height=53
        )

        #frame design
        # self.frame_image2 = ImageTk.PhotoImage(Image.open(path("bg7.png")))
        # self.frame_image2 = ImageTk.PhotoImage(Image.open(r"src\Client\pic\bg7.png"))

        # goi label de pritn cai icon nay len do
        # self.frame_image_label2 = Label(self, image=self.frame_image2, bg='black')
        # self.frame_image_label2.place(x=440, y=500)
    
