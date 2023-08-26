from socket import *
from tkinter import *

# s = socket.socket(addr_family, type)

# socket.AF_INET//ipv4
# socket.AF_INET6//ipv6

# socket.SOCK_STREAM //TCP
# socket.SOCK_DGRAM //UDP

#o day ta se chon ipv4 va TCP
#global variables
BUFSIZ = 1024 * 4
#lấy địa chỉ và port của máy hiện tại
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#giao dien
Windown_main = Tk()#tao object giao dien
Windown_main.geometry("800x600")
Windown_main.configure(bg="#23272E")

#Thiet lap tieu de
Windown_main.title('Remote-Pc-Client')

screen_access = LogIn_Page_UI(app) #gọi đến file giao diện login
#ket thuc giao dien










#ham shutdown
def shutdown_logout():
    client.sendall(bytes("SD_LO", "utf8"))
    temp = sl.shutdown_logout(client, app)
    return

#hàm main ui
def show_main_ui():
    frame_lg.destroy()
    global frame_hp
    #thêm hàm và chức năng mới vào đây để gọi
    frame_hp = HomePage_UI(app)
    frame_hp.button_shut_down.configure(command = shutdown_logout)
    return



#hàm kết nối với server thông qua 
def connect(frame):
    global client
    ip = frame.entry_1.get()
    try:
        client.connect((ip, 5656))
        messagebox.showinfo(message = "Connect successfully!")
        show_main_ui()
    except:
        messagebox.showerror(message = "Cannot connect!")       
    return 

#hàm main
def main():
    frame_lg.button_1.configure(command= lambda:connect(frame_lg))
    app.mainloop()

if __name__ == '__main__':
    main()




