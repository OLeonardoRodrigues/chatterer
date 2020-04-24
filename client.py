import socket, threading

# Socket creation
s = socket.socket()

# Constants declaration
host = socket.gethostname()
port = 12345

# Connecting to server
s.connect( ( host, port ) )

def main():
    threading.Thread( target = outConnection ).start()
    threading.Thread( target = inConnection ).start()

def outConnection():
    # Start main loop
    while( True ):         
        # Inputing & sending new message 
        receivedMessage = s.recv( 1024 )
        print( f'<<-- {receivedMessage.decode()} ' )

        # Loop breaking condition
        if( receivedMessage == '!exit' or receivedMessage == '!quit' ):
            s.close()
            break

def inConnection():
    # Start main loop
    while( True ):         
        # Inputing & sending new message 
        message = input( '' )
        s.send( message.encode() )

        # Loop breaking condition
        if( message == '!exit' or message == '!quit' ):
            s.close()
            break

if( __name__ == '__main__' ):
    main()