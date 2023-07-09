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
            print ("\n"+msg.decode('utf-8')+"\n"+PROMPT)
        except:
            msg = b''
    closeSocket(sock_tcp)

'''def userInteraction(sock_tcp):
    msg = ''
    while msg != '/q':
        try:
            msg = input(PROMPT)
            if msg != '': 
                print(sock_tcp, msg)
                sock_tcp.send(msg.encode('utf-8'))
        except:
            msg = '/q'
    closeSocket(sock_tcp)

'''

def userInteraction(sock_tcp):
    msg = ''
    while msg != '/q':
        msg = input(PROMPT)
        print(sock_tcp, msg)
        sock_tcp.send(msg.encode('utf-8'))
    closeSocket(sock_tcp)

