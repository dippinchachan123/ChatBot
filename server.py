#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pickle
import socket
from _thread import *
from Text import Text


server = ""
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
    print('connected')
except socket.error as e:
    print(str(e))

s.listen()

print("Waiting for a connection,Server started")

##
x_start = 2
pos = [Text(x_start),Text(x_start),0]
recv_snd_msg_list = []
client_name_dict = {0:"client",1:"client"}
client_msg_dict = {0:0,1:0}

def Threaded_client(conn, player):
    conn.send(pickle.dumps((pos[player], player)))
    reply = ""
    while True:
        global recv_snd_msg_list
        try:
            try:
                print(client_msg_dict,data_tuple[0])
            except:
                pass
            try:
                if len(data_tuple[0]):
                    if (data_tuple[0][-1]):
                        client_msg_dict[player] = len(data_tuple[0])
                else:
                    client_msg_dict[player] = 0
            except:
                pass
            data_tuple = pickle.loads(conn.recv(2048))
            client_name_dict[player] = data_tuple[1]


            if len(data_tuple[0]):
                if (data_tuple[0][-1]):
                    if len(recv_snd_msg_list) < len(data_tuple[0]):
                        print("msg_2",client_msg_dict, data_tuple[0][-1])
                        recv_snd_msg_list.append(data_tuple[0][-1] + [player])




            print("Recieving", data_tuple[0])
            if player == 1:

                reply = (recv_snd_msg_list,client_name_dict[0])
            if player == 0:

                reply = (recv_snd_msg_list, client_name_dict[1])


            print("Sending : ", reply)
            conn.sendall(pickle.dumps(reply))

        except error as e:
            break
    print("lost connection")
    conn.close()


run = True
current_player = 0
while run:
    conns, addrs = s.accept()

    print("Connected to ", addrs)
    start_new_thread(Threaded_client, (conns, current_player))
    current_player += 1




