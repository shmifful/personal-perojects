import socket
from _thread import *
import sys

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except scovket.error as e:
    str(e)

s.listen(4)
print("Waiting for a connection, Server started")

def threadedClient(conn):
    pass

while True:
    conn, addr = s.accepy()
    print("Connected to:", addr)

    startNewThread(threadedClient, (conn,))
