# Chatterer

Simple chat desktop application written for terminal in Python 3.8.x, using multithread and sockets.

## How to run it

There are two main ways to run this application, on only one machine or on two machines connected to the same network.

### On the same machine

Simply execute both scripts - server.py and client.py - on the same machine, but using separate terminals, server first.

No need to input address on the client script, it can use the default values to connect to the localhost on port 8080.

### Two machines on the same network

Execute the server script on one machine, and the client on the other, server must be executed first.

On the client, input the IP address for the server machine, you can input the port in which your client is going to work, if necessary.

## How to use it

Once you have both scripts running, they will try to connect to each other, and as soon as the connection is established you can start sending and receiving messages.

Both machines can send and receive messages, no need to wait for your turn.
