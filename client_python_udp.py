#client_python_udp.py
#Lucas Lopilato
#CS176A HW2
#
from socket import *
import sys

#Initialize port and hostname information 
serverName = ''
serverPort = -1

#Try to read in port and hostname information
try:
  #Read in Port number & serverName
  serverPort = int(sys.argv[2])
  serverName = sys.argv[1]
except IndexError:
  print('IndexError: Port Number Or Server Name Not Provided.')
  exit()
except ValueError:
  print('ValueError: ',sys.argv[1],' Is Not a Valid Port Number.')
  exit()
#Otherwise just print the unexpected error to stdout
except:
  print(sys.exc_info()[0])
  exit()

#Approach taken from Computer Networking (Kurose, Ross)
#
#Creates client's socket
#AF_INET specifies IPv4
#SOCK_DGRAM specifies UDP socket being used
#OS automatically configures port number for client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

#Asks user for input
message = input('Enter String:')

#message.encode() changes from string to byteType
#Sends encoded message to destination (serverName, serverPort)
clientSocket.sendto(message.encode(), (serverName, serverPort))


#Returning packets saved to modifiedMessage and serverAddress is saved into serverAddress
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
while(len(modifiedMessage.decode()) != 1 ):
  #Print output
  print(modifiedMessage.decode())

#Close socket
clientSocket.close()