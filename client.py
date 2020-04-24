import socket, threading, sys

def getDestinationAddress():
    host = ''
    port = 0

    host = input( 'Enter destination IP address: ' )
    port = input( 'Enter destination port: ' )

    if( not host ):
        host = socket.gethostname()
    
    if( not port ):
        port = 8080
    
    return( host, port )

def main():
    try:
        threading.Thread( target = rcvFromConnection ).start()
    except:
        print( f'Thread creation failed ' )
    
    try:
        threading.Thread( target = sendToConnection ).start()
    except:
        print( f'Thread creation failed ' )

def rcvFromConnection():
    # Start main loop
    while( True ):         
        # Receiving & printing new message 
        receivedMessage = s.recv( 1024 )
        print( f'{ host } -->> {receivedMessage.decode()} ' )

        # Loop breaking condition
        if( receivedMessage == '!exit' or receivedMessage == '!quit' ):
            s.close()
            break

def sendToConnection():
    # Start main loop
    while( True ):         
        # Inputing & sending new message 
        message = input( '' )
        s.send( message.encode() )

        # Loop breaking condition
        if( message == '!exit' or message == '!quit' ):
            s.close()
            break

try:
    # Socket creation
    s = socket.socket()
except:
    print( 'Socket creation error ' )
    sys.exit()
else: 
    print( 'Socket created succesfully! ' )

# Constants declaration
host, port = getDestinationAddress()

try:
    # Connecting to server
    s.connect( ( host, port ) )
except:
    print( f'Connection failed to address: { host }:{ port } ' )
    sys.exit()
else:
    print( f'Connected to { host }:{ port }! ' )

if( __name__ == '__main__' ):
    main()