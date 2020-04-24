import socket, threading, sys

def main():
    try:
        # Socket creation
        s = socket.socket()
    except:
        print( 'Socket creation error! ' )
        sys.exit()
    else: 
        print( 'Socket created succesfully! \n' )

    # Constants declaration
    host = socket.gethostname()
    port = 0
    port = input( 'Enter destination port: ' )
    print()
    
    if( not port ):
        port = 8080

    # Binding to Host
    s.bind( ( host, port ) )

    try:
        # Start listening for connections
        s.listen( 5 )
    except:
        print( 'Failed to start listening! ' )
    else:
        print( 'Now listening... \n' )

    # Accepting incoming connections
    connectionRcvd, srcAddress = s.accept()

    print( f'Received new connection from: { srcAddress[ 0 ] }:{ srcAddress [ 1 ] }\n' )

    threading.Thread( target = sendToConnection, args = ( connectionRcvd, srcAddress ) ).start()
    threading.Thread( target = rcvFromConnection, args = ( connectionRcvd, srcAddress ) ).start()

def sendToConnection( connectionRcvd, srcAddress ):
    # Start main loop
    while( True ):         
        # Inputing & sending new message 
        message = input( '' )
        connectionRcvd.send( message.encode() )

        # Loop breaking condition
        if( message == '!exit' or message == '!quit' ):
            connectionRcvd.close()
            break

def rcvFromConnection( connectionRcvd, srcAddress ):
    # Start main loop
    while( True ):         
        # Inputing & sending new message 
        receivedMessage = connectionRcvd.recv( 1024 )
        print( f'{ srcAddress[ 0 ] } -->> {receivedMessage.decode()} ' )

        # Loop breaking condition
        if( receivedMessage == '!exit' or receivedMessage == '!quit' ):
            connectionRcvd.close()
            break

if( __name__ == '__main__' ):
    main()    