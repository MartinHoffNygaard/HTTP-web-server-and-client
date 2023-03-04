# import socket module
from socket import *
from datetime import datetime
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Write your code here
serverPort = 12000                          # Sets the server port to a port that is normaly not used
serverSocket.bind(('', serverPort))         # Binds the server to the port and socket
serverSocket.listen()                       # Starts listening to connections to the server
# End of your code
while True:
    # Establish the connection print('Ready to serve...') connectionSocket, addr =
    try:
        # Write your code here
        print("The server is ready for connection")     # Prints a ready message to the terminal
        connectionSocket, addr = serverSocket.accept()  # accept a connection and stores connections in connectionSocket
        # End of your code
        # Write your code here
        input1 = connectionSocket.recv(1024).decode()   # Gets the HTTP request message sent to the server
        message = input1.split('\n')[0]                 # Gets the first line of the message since it contains the URL
        # End of your code
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        # Write your code here
        # sends a standard HTTP header to the client with HTTP version, 200 ok message and the type of content
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())
        # End of your code
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Write your code here
        connectionSocket.send("HTTP/1.1 404 Not found".encode())    # Sends an HTTP header with version and 404 error
        # End of your code
    # Close client socket
    # Write your code here
    connectionSocket.close()    # Closes the client socket
    # End of your code
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data

