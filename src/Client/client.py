from logInPage_GUI import LogIn_Page_UI
from homePage_GUI import HomePage_UI
from tkinter.messagebox import askyesno
import shutdown_logout_client as sl
import keylogger_client as kl
import app_process_client as ap
import live_screen_client as lsc

import socket
from tkinter import*
from tkinter import messagebox
from tkinter.ttk import*

#code ham



#main

#global variables
BUFSIZ = 1024 * 4
#lấy địa chỉ và port của máy hiện tại
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

app = Tk()
app.geometry("700x600")
app.configure(bg = "#FFFFFF")
app.title('Client')
app.resizable(False, False)
frame_lg = LogIn_Page_UI(app) #gọi đến file giao diện login



def back(temp):
    temp.destroy()
    frame_hp.tkraise()
    client.sendall(bytes("QUIT", "utf8"))

def liveCreen():
    client.sendall(bytes("LIVESCREEN", "utf8"))
    temp = lsc.Desktop_UI(app, client)
    if temp.status == False:
        back(temp)
    return


def disconnect():
    client.sendall(bytes("QUIT", "utf8"))
    frame_hp.destroy()
    app.destroy()
    return
 

def keylogger():
    client.sendall(bytes("KEYLOG", "utf8"))
    temp = kl.Keylogger_UI(app, client)
    temp.button_back.configure(command = lambda: back(temp))
    return

def app_process():
    client.sendall(bytes("APP_PRO", "utf8"))
    temp = ap.App_Process_UI(app, client)
    temp.button_back.configure(command = lambda: back(temp))
    return



def shutdown_logout():
    client.sendall(bytes("SD_LO", "utf8"))
    client.sendall(bytes("SHUTDOWN", "utf8"))
    return

def logout():
    client.sendall(bytes("SD_LO", "utf8"))
    client.sendall(bytes("LOGOUT", "utf8"))
    return

#show main ui
def show_main_ui():
    frame_lg.destroy()
    global frame_hp
    frame_hp = HomePage_UI(app)
    frame_hp.button_live_creen.configure(command = liveCreen)
    frame_hp.button_disconnect.configure(command = disconnect)
    frame_hp.button_keylogger.configure(command = keylogger)
    frame_hp.button_AppProcess.configure(command = app_process)
    frame_hp.button_shut_down.configure(command = shutdown_logout)
    frame_hp.button_logout.configure(command = logout)
    return

def connect(frame):
    global client
    ip = frame.entry_1.get()
    try:
        client.connect((ip, 5656))
        messagebox.showinfo(message = "Kết nối thành công!")
        show_main_ui()
    except:
        messagebox.showerror(message = "error!")       
    return 

def main():
    # show_main_ui()
    # LogIn_Page_UI(app) #gọi đến file giao diện login

    frame_lg.button_1.configure(command= lambda:connect(frame_lg))
    app.mainloop()

if __name__ == '__main__':
    main()