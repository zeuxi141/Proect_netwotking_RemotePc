import pickle
import os

BUFSIZ = 1024 * 4
SEPARATOR = "<SEPARATOR>"

# Hàm để hiển thị cây thư mục từ A đến Z trên máy chủ
def show_tree(client):
    ListDirectoryTree = []
    for c in range(ord('A'), ord('Z') + 1):
        path = chr(c) + ":\\"
        if os.path.isdir(path):
            ListDirectoryTree.append(path)
    data = pickle.dumps(ListDirectoryTree)
    client.sendall(str(len(data)).encode())
    temp = client.recv(BUFSIZ)
    client.sendall(data)

# Hàm để gửi danh sách thư mục từ máy chủ về máy khách
def send_list_dirs(client):
    path = client.recv(BUFSIZ).decode()
    if not os.path.isdir(path):
        return [False, path]

    try:
        list_tree = []
        ListDirectoryTree = os.listdir(path)
        for d in ListDirectoryTree:
            list_tree.append((d, os.path.isdir(path + "\\" + d)))
        
        data = pickle.dumps(list_tree)
        client.sendall(str(len(data)).encode())
        temp = client.recv(BUFSIZ)
        client.sendall(data)
        return [True, path]
    except:
        client.sendall("error".encode())
        return [False, "error"]    

# Hàm để xóa một tệp từ máy chủ
def delete_file(client):
    file_name = client.recv(BUFSIZ).decode()
    if os.path.exists(file_name):
        try:
            os.remove(file_name)
            client.sendall("ok".encode())
        except:
            client.sendall("error".encode())
            return
    else:
        client.sendall("error".encode())
        return

# Hàm để sao chép tệp từ máy khách lên máy chủ
def copy_file_to_server(client):
    received = client.recv(BUFSIZ).decode()
    if (received == "-1"):
        client.sendall("-1".encode())
        return
    filename, filesize, path = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
    client.sendall("received filename".encode())
    data = b""
    while len(data) < filesize:
        packet = client.recv(999999)
        data += packet
    if (data == "-1"):
        client.sendall("-1".encode())
        return
    try:
        with open(path + filename, "wb") as file:
            file.write(data)
        client.sendall("received content".encode())
    except:
        client.sendall("-1".encode())

# Hàm để sao chép tệp từ máy chủ xuống máy khách
def copy_file_to_client(client):
    filename = client.recv(BUFSIZ).decode()
    if filename == "-1" or not os.path.isfile(filename):
        client.sendall("-1".encode())
        return
    filesize = os.path.getsize(filename)
    client.sendall(str(filesize).encode())
    temp = client.recv(BUFSIZ)
    with open(filename, "rb") as f:
        data = f.read()
        client.sendall(data)

# Hàm thực hiện các thao tác thư mục và tệp tin trên máy chủ
def directory_operations(client):
    is_mod = False
    
    while True:
        if not is_mod:
            mod = client.recv(BUFSIZ).decode()

        if mod == "SHOW":
            show_tree(client)
            while True:
                check = send_list_dirs(client)
                if not check[0]:    
                    mod = check[1]
                    if mod != "error":
                        is_mod = True
                        break
        
        # Sao chép tệp từ máy khách lên máy chủ
        elif mod == "COPYTO":
            client.sendall("OK".encode())
            copy_file_to_server(client)
            is_mod = False

        # Sao chép tệp từ máy chủ xuống máy khách
        elif mod == "COPY":
            client.sendall("OK".encode())
            copy_file_to_client(client)
            is_mod = False

        elif mod == "DEL":
            client.sendall("OK".encode())
            delete_file(client)
            is_mod = False

        elif mod == "QUIT":
            return
        
        else:
            client.sendall("-1".encode())
