import socket
import time
from helper import checksum, data_to_binarr, bin_arr_to_data

HOST = "127.0.0.1"
PORT = 65432
ENCODE = 'utf-8'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print(f"[CONNECTED] connected to server on port {PORT}")
    data = input("Enter data: ").strip().removesuffix('\n')

    bin_data = data_to_binarr(data)

    time.sleep(1.5)
    # append checksum to data
    bin_data.append(checksum(bin_data))
    print("\n")
    print(bin_data)
    data_with_checksum = bin_arr_to_data(bin_data)
    time.sleep(1)
    print(f"\nData after appending checksum -> {data_with_checksum}\n")
    client.sendall(data_with_checksum.encode(ENCODE))
