import pickle
import psutil
import struct
import os
import subprocess

BUFSIZ = 1024 * 4

# Hàm gửi dữ liệu qua socket
def send_data(client, data):
    size = struct.pack('!I', len(data))
    data = size + data
    client.sendall(data)
    return

# Hàm lấy danh sách ứng dụng
def get_app_list():
    app_names = []
    app_ids = []
    app_thread_counts = []

    cmd = 'powershell "gps | where {$_.mainWindowTitle} | select Description, ID, @{Name=\'ThreadCount\';Expression ={$_.Threads.Count}}"'
    proc = os.popen(cmd).read().split('\n')
    temp = []
    for line in proc:
        if not line.isspace():
            temp.append(line)
    temp = temp[3:]
    for line in temp:
        try:
            arr = line.split(" ")
            if len(arr) < 3:
                continue
            if arr[0] == '' or arr[0] == ' ':
                continue

            app_name = arr[0]
            threads = arr[-1]
            app_id = 0
            cur = len(arr) - 2
            for i in range(cur, -1, -1):
                if len(arr[i]) != 0:
                    app_id = arr[i]
                    cur = i
                    break
            for i in range(1, cur, 1):
                if len(arr[i]) != 0:
                    app_name += ' ' + arr[i]
            app_names.append(app_name)
            app_ids.append(app_id)
            app_thread_counts.append(threads)
        except:
            pass
    return app_names, app_ids, app_thread_counts

# Hàm lấy danh sách các tiến trình
def get_process_list():
    process_names = []
    process_ids = []
    process_thread_counts = []
    for proc in psutil.process_iter():
        try:
            process_name = proc.name()
            process_id = proc.pid
            thread_count = proc.num_threads()
            process_names.append(str(process_name))
            process_ids.append(str(process_id))
            process_thread_counts.append(str(thread_count))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_names, process_ids, process_thread_counts

# Hàm tiêu diệt tiến trình
def terminate_process(pid):
    cmd = 'taskkill.exe /F /PID ' + str(pid)
    try:
        result = os.system(cmd)
        if result == 0:
            return 1
        else:
            return 0
    except:
        return 0
    
# Hàm khởi chạy ứng dụng
def start_app(app_name):
    subprocess.Popen(app_name)
    return

# Hàm xử lý giao tiếp với client
def handle_client(client):
    global msg
    while True:
        msg = client.recv(BUFSIZ).decode("utf8")
        if "QUIT" in msg and len(msg) < 20:
            return
        result = 0
        app_names = []
        app_ids = []
        app_thread_counts = []
        option = int(msg)
        if option == 0:  # Kill process
            pid = client.recv(BUFSIZ).decode("utf8")
            pid = int(pid)
            try:
                result = terminate_process(pid)
            except:
                result = 0
        elif option == 1:  # View processes or apps
            try:
                status = client.recv(BUFSIZ).decode("utf8")
                if "PROCESS" in status:
                    app_names, app_ids, app_thread_counts = get_app_list()
                else:
                    process_names, process_ids, process_thread_counts = get_process_list()
                result = 1
            except:
                result = 0
        elif option == 2:  # Delete (Not implemented in this code)
            result = 1
        elif option == 3:  # Start app
            app_to_start = client.recv(BUFSIZ).decode("utf8")
            try:
                start_app(app_to_start)
                result = 1
            except:
                result = 0
        if option != 1 and option != 3:
            client.sendall(bytes(str(result), "utf8"))
        if option == 1:
            app_names_data = pickle.dumps(app_names)
            app_ids_data = pickle.dumps(app_ids)
            app_thread_counts_data = pickle.dumps(app_thread_counts)

            send_data(client, app_names_data)   
            send_data(client, app_ids_data)
            send_data(client, app_thread_counts_data)
    return 