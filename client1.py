import socket
import sys

# Function that connects to the server, requests the file and prints the file to terminal


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Creates client socket
    try:
        client_socket.connect((server_name, server_port))               # Tries to connect to server with inputs
    except:
        print("Failed to connect to the server")                        # Error message if connection failed
        sys.exit()                                                      # Exits

    # Creates a GET request which we will use to get a file from the server. The 'f' is for making it easier to format
    # the request. Starts with GET then the name of the file. Afterwards is the hostname and the host port.
    get_request = f"GET /{filename} HTTP/1.1\r\nHost: {server_name}:{server_port}\r\n\r\n"

    client_socket.send(get_request.encode())                            # Sends the request to the server

    response = ''                           # Empty string variable to store the response
    while True:                             # To recieve all the response we need a loop to go through the response
        data = client_socket.recv(1024)     # Takes 1024 bytes from the response for each iteration of the loop
        if not data:                        # If there is no more data in the response we exit the loop
            break
        response += data.decode()           # Adds the information from the response to the response variable

    print(response)                         # Prints the full response to the terminal

    client_socket.close()                   # Closing the client socket


if __name__ == "__main__":                  # _init_ to store the variables and run the main function
    server_name = sys.argv[1]               # Stores the first argument that was stated when running the script as name
    server_port = int(sys.argv[2])          # Stores the second argument that was stated when running the script as port
    filename = sys.argv[3]                  # Stores the third argument that was stated when running the script as file
    main()                                  # Runs the main function


