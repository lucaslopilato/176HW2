# Lucas Lopilato
# CS176A HW2 Programming Assignment
# Server
from socket import *
import sys


# function to send a message back from a given socket
# destination address and message
def sendMessage(sock, clientAddress, msg):
    sock.sendto(msg.encode(), clientAddress)


# Maximum character length
MAX_INPUT = 128 * sys.getsizeof(str())

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
    message, clientAddress = serverSocket.recvfrom(2048)

    while(len(message) != 1):
        # Create Running sum
        sum = int(message[0])
        # Add each number to the sum
        for num in range(1, len(message)):
            sum += int(num)

    message = sum
    # Send out the sum as a message
    sendMessage(serverSocket, clientAddress, message)
    print('sending ', message)

except ValueError:
    sendMessage(serverSocket, clientAddress, 'Sorry, cannot compute!')
    print('sending sorry cannot compute')
