#!/usr/bin/python3

import socket

# Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host is the server IP
host = socket.gethostname()
# Port to listen on
port = 444

# Binding to the socket
# Host will be replaced/substitued with IP, if changed and not running on host
serversocket.bind((host, port)) 


# Starting the TCP listener
serversocket.listen(5)

while True:
    # Starting the connection
    clientsocket, address = serversocket.accept()

    print("Connection received from %s " % str(address))

    # Message sent to the client after a successful connection
    message = "Thank you for connecting to the server" + "\r\n"
    
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
