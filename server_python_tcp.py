# Lucas Lopilato
# CS176A HW2 Programming Assignment
# Server
from socket import *
import sys


# function to send a message back from a given socket
# destination address and message
def sendMessage(sock, msg):
    outgoing = msg.encode()
    sock.send(str(len(msg)).zfill(4).encode())
    sock.send(outgoing)


# Maximum character length
MAX_INPUT = 128

# Define port variable (uninitialized)
serverPort = -1

# Try to read in desired port number
try:
    # Read and cast port number to an integer
    serverPort = int(sys.argv[1])
except IndexError:
    print('IndexError: Port Number Not Provided.')
except ValueError:
    print('ValueError: ', sys.argv[1], ' Is Not a Valid Port Number.')
# Otherwise just print the unexpected error to stdout
except:
    print(sys.exc_info()[0])

# Create TCP Server
# Approach taken from Computer Networking (Kurose, Ross)

# Set up server as TCP server using IPv4
serverSocket = socket(AF_INET, SOCK_STREAM)
# Add socket flag to try and reuse an already used port
# Incase testing is done with same port
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Assigns port number to TCP socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
# Retrieve connection information
connectionSocket, addr = serverSocket.accept()

try:
    # Retrieve message from client and decode it
    message = connectionSocket.recv(MAX_INPUT).decode()

    #While there are more than 1 numbers to process
    while(len(message) > 1):
        # Create Running sum
        sum = 0
        # Add each number to the sum
        for num in range(0, len(message)):
            sum += int(message[num])

        #convert message to a string
        message = str(sum)
        # Send out the sum as a message
        sendMessage(connectionSocket, message)

    sendMessage(connectionSocket, message)

# If there is a non integer provided, send error message
except:
    sendMessage(connectionSocket, 'Sorry, cannot compute!')
    connectionSocket.close()
    exit()

connectionSocket.close()
