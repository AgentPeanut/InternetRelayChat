#Portland State University
#Professor Nirupama Bulusu
#IRC Project

#This module contains the socket connection
import socket
import threading #for multiple process


host = '127.0.0.1' #localhost
port = 55555  #do not use 0 to 40000, as they are reserved

#starting the server
#AF_INET is for the type of addresses that makes connection (Internet) and SOCK_STREAM is for tcp connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port)) #server is binding
server.listen() #now its in listening mode


instructions = '\nList of commands:\n' \
               '<list> to list all the rooms\n' \
               '<quit> to quit\n' \
               '<help> to list all the commands\n' \
               '<leave> to leave the room \n' \
               '<join> roomname to join or create the room\n' \
               '<switch> roomname to switch room\n' \
               '<personal> name message to send personal message'

#now create a empty list and dict for data storage
clients = []
nicknames = []
roomdetails = {}
users = {}
users_in_room = {}

#to broadcast the message
def broadcast(message, roomname):
    for client in roomdetails[roomname].peoples:
        msg = '['+roomname+'] '+message
        client.send(msg.encode('ascii'))
