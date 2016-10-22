README.txt
Lucas Lopilato

This document describes my approach to solving both TCP and UDP client/server connections.
Much of the approach was taken from Computer Networking (Kurose, Ross). I used a lot of the TCP and UDP solutions for opening a connection, listening,
closing, and packaging messages.

client_python_udp.py
--------------------------------------------------
This file represents the client side for a UDP connection. It's responsibilities are
Reading in a servername and port name, reading in a string from input, 
sending it to the server at the specified address and port, and receiving 
answers back.

It sets up the UDP socket and once the string is read in, it sends the encoded string immediately.

After the message is sent, the client enters a while loop to continuously monitor for packets.

Each message received is decoded and printed to the output.

If the length of the received message is less than or equal to 1 or the error message, it closes the socket. 
Otherwise it will keep listening.
-------------------------------------------------
server_python_udp.py
-------------------------------------------------
This file is responsible for listening for packets from client_python_udp.py

The beginning defines a helper function that will send a message to a socket and portAddress.

A global variable of MAX_INPUT is defined to limit the maximum amount of data that can be read in.

After that, the server reads in the port number from command line arguments.

From there, the server opens the socket connection and binds the respective port. 
It then listens to and reads in an incoming packet.

The incoming message is decoded and the length is calculated. 
If the length is greater than one, the server moves into a continual loop. 
It attempts to convert the number into an integer, and adds the digits together to create a sum.

If an error is thrown, the server sends the error message to the client, closes the connection, and exits. 
If an error is not thrown the sum is sent to the client and the digits of the sum 
is continually readded and sent to the client until the sum is a single digit.

From there, the server will check if the single input is an integer, then send it back if it is.

-------------------------------------------------
client_python_tcp.py
-------------------------------------------------
The TCP client works by reading in both serverName and serverPort. 
From there it requests a TCP connection with the TCP server, then asks for a user string. 
It immediately sends the encoded string to the server.

Afterwards, it enters a loop to listen for response packets. 
The server sends a string of 4 bits to tell the TCP client how many bytes the incoming packet will contain. 
The client takes this information and reads in the exact amount of bytes from the input buffer. It decodes the message and prints to output.

If the length of the incoming message is 1 or less, or it is an error message, the client closes the connection.

-------------------------------------------------
server_python_tcp.py
-------------------------------------------------
The TCP server begins with a sendMessage function. This function encodes the outgoing 
message, and sends the buffer size of the message into a 4 digit string. 
The buffer size is sent, then the outgoing message is sent.

Next, a global variable of 128 (max input) is specified. The server then reads in the port number to be listening on.

After port is read in, the server opens the TCP connection, specifies to reuse the port if it is used, and binds the port number. 
It then listens on the port for a connection and accepts a connection when it completes a handshake.

From there, the server will receive and process the first packet it receives. If the length is greater than one, it will add up the digits as before. Otherwise it will typecheck it. If the input is not a number, it will send the error message and close the socket. Otherwise it will send the input back to the client and close the connection.