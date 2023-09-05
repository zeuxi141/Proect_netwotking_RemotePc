import tkinter as tk
from tkinter import  ttk
import pickle, struct
from tkinter import*
from PIL import Image, ImageTk

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

def recvall(sock, size):
    message = bytearray()
    while len(message) < size:
        buffer = sock.recv(size - len(message))
        if not buffer:
            raise EOFError('Could not receive all expected data!')
        message.extend(buffer)
    return bytes(message)

def receive(client):
    packed = recvall(client, struct.calcsize('!I'))
    size = struct.unpack('!I', packed)[0]
    data = recvall(client, size)
    return data

def switch(button, tab):
    if button['text'] == 'Process':
        button.configure(text = 'Application')
        tab.heading("Name", text = "Name Process")
        tab.heading("ID", text = "ID Process")
        tab.heading("Count", text = "Count Threads")
    else:
        button.configure(text = 'Process')
        tab.heading("Name", text = "Name Application")
        tab.heading("ID", text = "ID Application")
        tab.heading("Count", text = "Count Threads")
    return

def send_kill(client):
    global pid
    client.sendall(bytes("0", "utf8"))
    client.sendall(bytes(str(pid.get()), "utf8"))
    message = client.recv(BUFSIZ).decode("utf8")
    if "1" in message:
        tk.messagebox.showinfo(message = "killed")
    else:
        tk.messagebox.showerror(message = "error!!!")
    return

def _list(client, tab, s):
    client.sendall(bytes("1", "utf8"))
    client.sendall(bytes(s, "utf8"))
    list1 = receive(client)
    list1 = pickle.loads(list1)
    list2 = receive(client)
    list2 = pickle.loads(list2) 
    list3 = receive(client)
    list3 = pickle.loads(list3)
    print(list1)
    print(list2)
    print(list3)
    for i in tab.get_children():
        tab.delete(i)
    for i in range(len(list1)):
        tab.insert(parent = '', index = 'end', text = '', values = (list1[i], list2[i], list3[i]))
    return

def clear(tab):
    for i in tab.get_children():
        tab.delete(i)
    return

def send_start(client):
    global pname
    client.sendall(bytes("3", "utf8"))
    client.sendall(bytes(str(pname.get()), "utf8"))
    return
        
def start(root, client):
    global pname
    pstart = tk.Toplevel(root)
    pstart['bg'] = 'black'
    pstart.geometry("420x50")
    pname = tk.StringVar(pstart)
    tk.Entry(pstart, textvariable = pname, width = 38, borderwidth = 5).place(x= 8, y= 20)
    tk.Button(pstart, text = "Start", width = 14, height = 2, fg = 'white', bg = 'IndianRed3', borderwidth=0,
            highlightthickness=0, command = lambda: send_start(client), relief="flat").place(x= 300, y= 15)
    return
    
def kill(root, client):
    global pid
    kill = tk.Toplevel(root)
    kill['bg'] = 'black'
    kill.geometry("420x50")
    pid = tk.StringVar(kill)
    tk.Entry(kill, textvariable = pid, width = 38, borderwidth = 5).place(x= 8, y= 20)
    tk.Button(kill, text = "Kill", width = 14, height = 1, fg = 'white', bg = 'IndianRed3', borderwidth=0,
            highlightthickness=0, command = lambda: send_kill(client), relief="flat").place(x= 300, y= 15)
    return
        
class App_Process_UI(Frame):
     def __init__(self, parent, client):    
        Frame.__init__(self, parent)
        self.configure(
            #window,
            bg = "black",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        parent.geometry("1000x600+200+200")
        self.grid(row=0, column=0, sticky="nsew")

        #backround
        # self.back_gound_image = ImageTk.PhotoImage(Image.open(path("bg8.png")))
        self.back_gound_image = ImageTk.PhotoImage(Image.open(r"src\Client\pic\mmt.jpg"))

        self.back_gound_label = Label(self, image=self.back_gound_image, bg='black')
        self.back_gound_label.pack(fill=X)

        # dung tree view 
        self.tab = ttk.Treeview(self, height = 18, selectmode='browse')
        self.scroll = tk.Scrollbar(self, orient = "vertical", command = self.tab.yview)
        self.scroll.place(
            x=850,
            y=40,
            height=404
        )
        self.tab.configure(yscrollcommand = self.scroll.set)
        self.tab['columns'] = ("Name", "ID", "Count")
        self.tab.column('#0', width=0)
        self.tab.column("Name", anchor="center", width = 150, minwidth = 10, stretch = True)
        self.tab.column("ID", anchor="center", width = 150, minwidth = 10, stretch = True)
        self.tab.column("Count", anchor="center", width = 150, minwidth = 10, stretch = True)
        self.tab.heading('#0', text='')
        self.tab.heading("Name", text = "Name Application")
        self.tab.heading("ID", text = "ID Application")
        self.tab.heading("Count", text = "Count Threads")
        self.tab.place(
            x=140,
            y=40,
            width=713,
            height=404
        )

        self.button_process = Button(self, text = 'Process', width = 20, height = 5, fg = '#ffffff', bg = '#783497',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch(self.button_process, self.tab),
            relief="flat"
        )
        self.button_process.place(
            x=80,
            y=460,
            width=135,
            height=50
        )

        self.button_list = Button(self, text = 'Show', width = 20, height = 5, fg = '#ffffff', bg = '#783497',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: _list(client, self.tab, self.button_process['text']),
            relief="flat"
        )
        self.button_list.place(
            x=80,
            y=520,
            width=135,
            height=50
        )

        self.button_start = Button(self, text = 'Start', width = 20, height = 5, fg = '#ffffff', bg = '#783497',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: start(parent, client),
            relief="flat"
        )
        self.button_start.place(
            x=450,
            y=460,
            width=135,
            height=50
        )

        self.button_kill = Button(self, text = 'Kill', width = 20, height = 5, fg = '#ffffff', bg = '#783497',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: kill(parent, client),
            relief="flat"
        )
        self.button_kill.place(
            x=450,
            y=520,
            width=135,
            height=50
        )

        self.button_clear = Button(self, text = 'Clear', width = 20, height = 5, fg = '#ffffff', bg = '#783497',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: clear(self.tab),
            relief="flat"
        )
        self.button_clear.place(
            x=820,
            y=460,
            width=135,
            height=50
        )
        
        self.button_back = Button(self, text = 'Back', width = 20, height = 5, fg = '#ffffff', bg = '#783497',
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_back.place(
            x=820,
            y=520,
            width=135,
            height=50
        )