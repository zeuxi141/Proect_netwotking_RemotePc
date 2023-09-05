from tkinter import*
import os # cung cap chuc nang tuong tac voi he dieu hanh
import sys
from PIL import Image, ImageTk # cho phep ta truy cap cac tham so va chuc nang cu the cua he dieu hanh


def path(file_name):
    file_name = 'pic\\' + file_name
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller _MEIPASS tap mot thu muc va luu tru mot duong dan _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".") # tra ve duong dan path name

    return os.path.join(base_path, file_name) # ket hop mot duong dan voi file name

class HomePage_UI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.configure(
            bg = "black",
            height = 800,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        parent.geometry("1000x600")
        self.grid(row=0, column=0, sticky="nsew")
        
        #backround
        # self.back_gound_image = ImageTk.PhotoImage(Image.open(path("bg1.png")))
        self.back_gound_image = ImageTk.PhotoImage(Image.open(r"src\Client\pic\mmt.jpg"))

        self.back_gound_label = Label(self, image=self.back_gound_image, bg='black')
        self.back_gound_label.pack(fill=X)

        # button - live creen
        self.button_live_creen = Button(
            self,
            borderwidth=0,
            text="Live Screen",
            bg='#783497',
            fg= '#ffffff',
            font='Helvetica 20 bold',
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_live_creen.place(
            x=80,
            y=80,
            width=200,
            height=60
        )
        # button - keylogger
        self.button_keylogger = Button(
            self,
            borderwidth=0,
            text="Key Logger",
            bg='#783497',
            fg= '#ffffff',
            font='Helvetica 20 bold',
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_keylogger.place(
            x=180,
            y=180,
            width=200,
            height=60
        )

        # button - app process
        self.button_AppProcess = Button(
            self,
            borderwidth=0,
            text="App Process",
            bg='#783497',
            fg= '#ffffff',
            font='Helvetica 20 bold',
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_AppProcess.place(
            x=720,
            y=80,
            width=200,
            height=60
        )

        # button - logout
        self.button_logout = Button(
            self,
            borderwidth=0,
            text="Logout",
            bg='#783497',
            fg= '#ffffff',
            font='Helvetica 20 bold',
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_logout.place(
            x=620,
            y=180,
            width=200,
            height=60
        )
        #button shutdown
        self.button_shut_down = Button(
            self,
            borderwidth=0,
            text="Shut Down",
            bg='#783497',
            fg= '#ffffff',
            font='Helvetica 20 bold',
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_shut_down.place(
            #x=727.0,
            #y=72.0,
            x=400,
            y=280,
            width=200,
            height=60
        )

        #disconnect
        self.button_disconnect = Button(
            self,
            borderwidth=0,
            text="Disconnect",
            bg='#783497',
            fg= '#ffffff',
            font='Helvetica 20 bold',
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_disconnect.place(
            #x=727.0,
            #y=72.0,
            x=400,
            y=380,
            width=200,
            height=60
        )

        # self.back_gound_image3 = ImageTk.PhotoImage(Image.open(r"src\Client\pic\bg3.jpg"))

        # self.back_gound_label3 = Label(self, image=self.back_gound_image3, bg='black')
        # self.back_gound_label3.place(x=750,y=60)

        # # Button disconnect
        # self.disconnect_label = Label(
        #     self,
        #     text="DISCONNECT",
        #     fg='red', 
        #     bg='black',
        #     font='Helvetica 24 bold'
        # )

        # self.disconnect_label.place(
        #     x=760,
        #     y=300,
        # )

        # # self.disconnect_image = ImageTk.PhotoImage(Image.open(path("bt3.jpg")))
        # self.disconnect_image = ImageTk.PhotoImage(Image.open(r"src\Client\pic\bt3.jpg"))


        # self.button_disconnect = Button(
        #     self,
        #     image=self.disconnect_image,
        #     bg='black',
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: print("button_disconnect clicked"),
        #     relief="flat"
        # )

        # self.button_disconnect.place(
        #     x=820,
        #     y=380,
        # )



