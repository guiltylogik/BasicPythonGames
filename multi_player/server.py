import socket
from _thread import *
import sys
from game import Game
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

soc.listen()
print("Waiting for a connection, Server Started")

connected = set()
games = {}
id_count = 0

def threaded_client(conn, current_player, game_id):
    global id_count
    conn.send(str.encode(str(current_player)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if game_id in games:
                game = games[game_id]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset_moves()
                    elif data != "get":
                        game.play(current_player, data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print("Lost connection")

    try:
        del games[game_id]
        print("Closing game ", game_id)

    except:
        pass
    id_count -= 1
    conn.close()

while True:
    conn, addr = soc.accept()
    print("Connected to: ", addr)

    id_count += 1
    current_player = 0
    game_id = (id_count - 1) // 2

    if id_count % 2 == 1:
        games[game_id] = Game(game_id)
        print("Creating a new game....")
    else:
        games[game_id].ready = True
        current_player = 1

    start_new_thread(threaded_client, (conn, current_player, game_id))
