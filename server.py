import socket
import time
from helper import data_to_binarr, checksum
HOST = "127.0.0.1"
PORT = 65432
ENCODE = 'utf-8'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Listening on port {PORT}...")
    client, addr = server.accept()
    print(f"[CONNECTED] Connected to {addr}")
    data = client.recv(1024)
    data = data.decode()
    print(f"Data Received {data}")

    bin_data = data_to_binarr(data)
    # data_with_checksum = bin_arr_to_data(bin_data)

    # print(f"Data after appending checksum -> {data_with_checksum}")
    time.sleep(1)
    result = checksum(bin_data)

    time.sleep(1)
    if result == '00000000':
        print(f"[Success] Data received successfully")
    else:
        print(f"[Error] Data reeived with error.")
