import socket
from _thread import *
import sys
from player import Player
import pickle


# colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)

server = '192.168.43.94'
port = 5555

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    soc.bind((server, port))
except socket.error as e:
    str(e)

soc.listen(2)
print("Waiting for a connection, Server Started")

players = [Player(0,0,50,50,RED), Player(100,100,50,50,BLUE)]

def threaded_client(conn, current_player):
    conn.send(pickle.dumps(players[current_player]))
    reply = ''
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[current_player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if current_player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Recieved: ", data)
                print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))
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
