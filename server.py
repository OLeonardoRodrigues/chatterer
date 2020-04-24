import socket, threading

def main():
    # Socket creation
    s = socket.socket()

    # Constants declaration
    host = socket.gethostname()
    port = 12345

    # Binding to Host
    s.bind( ( host, port ) )

    # Start listening for connections
    s.listen( 5 )

    # Accepting incoming connections
    connectionRcvd, srcAddress = s.accept()

    threading.Thread( target = inNewConnection, args = ( connectionRcvd, srcAddress ) ).start()
    threading.Thread( target = outNewConnection, args = ( connectionRcvd, srcAddress ) ).start()

def inNewConnection( connectionRcvd, srcAddress ):
    # Logging new connection
    print( f'Received new connection from: { srcAddress }' )

    # Start main loop
    while( True ):         
        # Inputing & sending new message 
        message = input( '' )
        connectionRcvd.send( message.encode() )

        # Loop breaking condition
        if( message == '!exit' or message == '!quit' ):
            connectionRcvd.close()
            break

def outNewConnection( connectionRcvd, srcAddress ):
    # Logging new connection
    print( f'Received new connection from: { srcAddress }' )

    # Start main loop
    while( True ):         
        # Inputing & sending new message 
        receivedMessage = connectionRcvd.recv( 1024 )
        print( f'<<-- {receivedMessage.decode()} ' )

        # Loop breaking condition
        if( receivedMessage == '!exit' or receivedMessage == '!quit' ):
            connectionRcvd.close()
            break

if( __name__ == '__main__' ):
    main()    