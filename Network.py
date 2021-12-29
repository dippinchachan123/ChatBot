#!/usr/bin/env python
# coding: utf-8

# In[15]:


import socket
import pickle
from _thread import *

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.100"
        self.port = 5555
        self.addrs = (self.server, self.port)
        self.p = self.connect()

    def get_p(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addrs)
            recieved = pickle.loads(self.client.recv(2048))
            return recieved
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))

        except socket.error as e:
            print(e)
            self.client.close()



