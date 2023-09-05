import tkinter as tk
import socket
import keylogger_server as kl 
import app_process_server as ap
import live_screen_server as lss
import shutdown_logout_server as sl
import ctypes
import pymsgbox as a

is_opened = False  # Khai báo biến is_opened 

main = tk.Tk()
main.geometry("400x300")
main.title("Server")
main['bg'] = '#000000'

#Global variables
global client
BUFSIZ = 1024 * 4

def live_screen():
    global client
    lss.capture_screen(client)
    return


def keylogger():
    global client
    kl.keylog(client)
    return


def app_process():
    global client
    ap.app_process(client)
    return



def shutdown_logout():
    global client
    sl.shutdown_logout(client)
    return

#Connect
###############################################################################           
def Connect():
    b = a.alert("chạy server thành công", 'Title')
    print(b)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 5656
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(100)
    global client
    client, addr = s.accept()
    while True:
        msg = client.recv(BUFSIZ).decode("utf8")
        if "KEYLOG" in msg:
            keylogger()
        elif "SD_LO" in msg:
            shutdown_logout()
        elif "LIVESCREEN" in msg:
            live_screen()
        elif "APP_PRO" in msg:
            app_process()
        elif "QUIT" in msg:
            client.close()
            s.close()
            return
###############################################################################    

def toggle_state():
    global is_opened
    
    # global button  # Thêm dòng này để tham chiếu đến biến 'button'
    if is_opened:
        button.config(text="Start server")
        is_opened = False
    else:
        button["text"]="is running"
        button["bg"]="orange"
        # ctypes.windll.user32.MessageBoxW(0, "server is running")
        Connect()
        is_opened = True

button = tk.Button(main, text="Start server", width=15, height=2, fg='white', bg='#783497', borderwidth=0,
                   highlightthickness=0, command=toggle_state, relief="flat", font='Helvetica 15 bold')
button.place(x=200, y=150, anchor="center")
# button.config(text="is running")




    
main.mainloop()


