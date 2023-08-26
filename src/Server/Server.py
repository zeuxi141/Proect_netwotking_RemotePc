from socket import *
from tkinter import *


# s = socket(AF_INET, SOCK_STREAM)

# s.bind(("192.168.1.14", 9000))

# s.listen(5)

# while True:
#     c,a = s.accept()
#     print ("recevied connection from", a)
#     c.send("hello %s\n"%a[0])
#     c.close()
main = tk.Tk()
main.geometry("200x200")
main.title("Server")
main['bg'] = '#000000'

#Global variables
global client
BUFSIZ = 1024 * 4

def shutdown_logout():
    global client
    sl.shutdown_logout(client)
    return


def Connect():
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
        if "SD_LO" in msg:
            shutdown_logout()
            s.close()
            return


tk.Button(main, text = "OPEN", width = 10, height = 2, fg = 'white', bg = 'IndianRed3', borderwidth=0,
            highlightthickness=0, command = Connect, relief="flat").place(x = 100, y = 100, anchor = "center")
main.mainloop()