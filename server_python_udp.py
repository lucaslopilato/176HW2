# Lucas Lopilato
# CS176A HW2 Programming Assignment
# Server
# Socket connection taken from Computer Networking (Kurose, Ross)
# code includes opening a connection, encoding a message,
# and listening on a port.
from socket import *
import sys


# function to send a message back from a given socket
# destination address and message
def sendMessage(sock, clientAddress, msg):
    sock.sendto(msg.encode(), clientAddress)


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

# Create UDP Server
# Approach taken from Computer Networking (Kurose, Ross)

# Set up server as UDP server using IPv4
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Add socket flag to try and reuse an already used port
# Incase testing is done with same port
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Assigns port number to UDP socket
serverSocket.bind(('', serverPort))

try:
    # Retrieve message from client and decode it
    message, clientAddress = serverSocket.recvfrom(MAX_INPUT)
    message = message.decode()
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
        sendMessage(serverSocket, clientAddress, message)
    message = str(int(message))
    sendMessage(serverSocket,clientAddress,message)

# If there is a non integer provided, send error message
except:
    sendMessage(serverSocket, clientAddress, 'Sorry, cannot compute!')
    serverSocket.close()
    exit()

serverSocket.close()
