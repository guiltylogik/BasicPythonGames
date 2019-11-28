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

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

positions = [(0, 0), (100, 100)]

def threaded_client(conn, current_player):
    conn.send(str.encode(make_pos(positions[current_player])))
    reply = ''
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            positions[current_player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if current_player == 1:
                    reply = positions[0]
                else:
                    reply = positions[1]
                print("Recieved: ", data)
                print("Sending: ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()

current_player = 0

while True:
    conn, addr = soc.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
