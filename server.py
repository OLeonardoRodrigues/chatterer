import socket, threading
from _thread import start_new_thread

print_lock = threading.Lock()

def threaded(c):
    while True:
        data = c.recv(1024)
        print(str(data.decode("ascii")))
        if not data:
            print('Disconnected... ')
            print_lock.release()
            break
    c.close()

def Main():
    host= ''

    port=12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port))

    print(f'Socket binded to port: {port} ')

    s.listen(5)
    print('Socket is listening... ')

    while True:
        c = s.accept()

        print_lock.acquire()

        start_new_thread(threaded, (c,))

    s.close()

if __name__ == '__main__':
    Main()
