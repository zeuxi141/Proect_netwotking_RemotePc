import tkinter as tk

# Hàm được gọi khi cửa sổ đóng và gửi yêu cầu QUIT đến máy chủ
def closeEvent(main, client):
    client.sendall(bytes("QUIT", "utf8"))  # Gửi yêu cầu QUIT dưới dạng dãy bytes
    main.destroy()  # Đóng cửa sổ chính
    return

# Hàm gửi yêu cầu SHUTDOWN đến máy chủ
def shutdown(client):
    client.sendall(bytes("SHUTDOWN", "utf8"))  # Gửi yêu cầu SHUTDOWN dưới dạng dãy bytes

# Hàm gửi yêu cầu LOGOUT đến máy chủ
def logout(client):
    client.sendall(bytes("LOGOUT", "utf8"))  # Gửi yêu cầu LOGOUT dưới dạng dãy bytes

# Hàm kết hợp yêu cầu SHUTDOWN và LOGOUT, hiển thị cửa sổ mới để xác nhận
def shutdownAndlogout(client, root):
    window = tk.Toplevel(root)  # Tạo cửa sổ con mới (Toplevel) dựa trên cửa sổ gốc (root)
    window.geometry("190x160")  # Thiết lập kích thước của cửa sổ con
    window.grab_set()  # Khóa cửa sổ gốc để ngăn người dùng tương tác với nó khi cửa sổ con đang mở
    window.protocol("WM_DELETE_WINDOW", lambda: close_event(window, client))  # Gán hàm close_event khi cửa sổ con bị đóng
    shutdown_button = tk.Button(
        window, text='SHUTDOWN', width=20, height=2, fg='white', bg='IndianRed3',
        command=lambda: shutdown(client), padx=20, pady=20)
    shutdown_button.grid(row=0, column=0)  # Đặt nút SHUTDOWN vào cửa sổ con
    logout_button = tk.Button(
        window, text='LOGOUT', width=20, height=2, fg='#e64040', bg='#4d4d4d',
        command=lambda: logout(client), padx=20, pady=20)
    logout_button.grid(row=1, column=0)  # Đặt nút LOGOUT vào cửa sổ con
    window.mainloop()  # Bắt đầu vòng lặp sự kiện của cửa sổ con