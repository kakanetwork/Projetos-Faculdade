import socket
from variables import *

def closeSocket(sock_tcp):
    try:
        sock_tcp.close()
    except:
        None

def servInteraction(sock_tcp):
    msg = b' '
    while msg != b'':
        try:
            msg = sock_tcp.recv(512)
            print ("\n"+msg.decode(UNICODE)+"\n"+PROMPT)
        except:
            msg = b''
    closeSocket(sock_tcp)

def userInteraction(sock_tcp):
    msg = ''
    while msg != '/q':
        try:
            msg = input(PROMPT)
            if msg != '': 
                sock_tcp.send(msg.encode(UNICODE))
        except:
            msg = '/q'
    closeSocket(sock_tcp)


