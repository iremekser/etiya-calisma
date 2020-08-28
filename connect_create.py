import socket
import threading    

server = '192.168.1.192'
port = 4443

def my_tcp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((server, port))
    sock.listen()
    while True:
        conn, address = sock.accept()
        print(address)
        conn.close()
        
        
my_tcp_server()
# def main():
# ....

