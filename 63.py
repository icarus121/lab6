import socket
import sys
import time
import errno
from multiprocessing import Process
import math

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    while True:
     s_sock.send(str.encode('Choose Your Mathematical function'))
     #s_sock.send(str.encode('Choose Your Mathematical function ->'))
     while True:
        data = s_sock.recv(4096)
        data = data.decode('utf-8')
        print(data)
        if not data:
            break
        elif data == 'log':
            #s_sock.send(str.encode(math.log()))
            s_sock.send(str.encode('Enter your Number'))
            input = s_sock.recv(4096)
            #input = input.decode('utf-8')
            input = int(input)
            input = str(math.log(input))
            print(type(input))
            #input = str(input)

        elif data == 'sqrt':
            s_sock.send(str.encode('Enter your Number'))
            input = s_sock.recv(4096)
            #input = input.decode('utf-8')
            input = int(input)
            input = str(math.sqrt(input))
            print(type(input))

        elif data == 'expn':
            s_sock.send(str.encode('Enter your Number'))
            input = s_sock.recv(4096)
            #input = input.decode('utf-8')
            input = int(input)
            input = str(math.exp(input))
            print(type(input))

        else:
            s_sock.send(str.encode('Not found'))

        s_sock.send(str.encode("Result:" + input))
        #s_sock.sendall(str.encode(ok_message))
     s_sock.close()


if __name__ == '__main__':
    s = socket.socket()
    s.bind(('',8081))
    print("listening...")
    s.listen(5)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:
                print('got a socket error')
    except Exception as e:
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
     	   s.close()

