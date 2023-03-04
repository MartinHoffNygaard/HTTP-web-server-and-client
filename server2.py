from socket import *
import sys
import _thread as thread


def main():
    serverSocket = socket(AF_INET, SOCK_STREAM) # Creates server socket
    serverPort = 12000  # Sets the server port to a port that is normally not used
    serverSocket.bind(('', serverPort))  # Binds the server to the port and socket
    serverSocket.listen(10)  # Starts listening to connections to the server

    while True:
        print("The server is ready for connection")  # Prints a ready message to the terminal
        connectionSocket, addr = serverSocket.accept()  # accept a connection and stores connections in connectionSocket
        thread.start_new_thread(handleClient, (connectionSocket,))  # Starts a new thread to handle the client

    serverSocket.close()
    sys.exit()


"""Function to handle a client. The function will take the request sent from the client and return the file requested by
the client. Having it in a function makes it possible to use it in different threads at the same time so we can handle 
client separately at the same time"""


def handleClient(client):
    while True:
        try:
            input1 = client.recv(1024).decode()  # Gets the HTTP request message sent to the server
            message = input1.split('\n')[0]  # Gets the first line of the message since it contains the URL
            filename = message.split()[1]  # Gets the filename
            f = open(filename[1:])  # Opens the file
            outputdata = f.read()  # Reads the file
            # sends a standard HTTP header to the client with HTTP version, 200 ok message and the type of content
            client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())
            for i in range(0, len(outputdata)):         # Goes through the contents of the file ands sends it to client
                client.send(outputdata[i].encode())
            client.send("\r\n".encode())
            client.close()
        except IOError:
            # Send response message for file not found
            client.send("HTTP/1.1 404 Not found".encode())    # Sends an HTTP header with version and 404 error
        client.close()  # Closes the client socket


if __name__ == '__main__':
    main()
