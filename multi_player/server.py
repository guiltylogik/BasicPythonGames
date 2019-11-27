import socket
from _thread import *
import sys

server = '192.168.43.94'
port = 5555

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    soc.bind((server, port))
except socket.error as e:
    str(e)

soc.listen(2)
print("Waiting for a connection, Server Started")

def threaded_client(conn):

    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

while True:
    conn, addr = soc.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))