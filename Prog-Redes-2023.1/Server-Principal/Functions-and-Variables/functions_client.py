import socket
from variables import *
from functions_others import *

# ============================================================================================================

def closeSocket(sock_tcp):
    try:
        sock_tcp.close()
    except:
        None
        
# ============================================================================================================

def servInteraction(sock_tcp):
    try:
        msg = b' '
        while msg != b'':
            try:
                msg = sock_tcp.recv(512)
                print(msg.decode(UNICODE))
            except:
                msg = b''
    except:
        print(f'\nErro no ServInteraction...{sys.exc_info()[0]}')  
        exit() 
    closeSocket(sock_tcp)

# ============================================================================================================

def userInteraction(sock_tcp):
    try:
        msg = ''
        while msg != '/q':
            try:
                msg = input(PROMPT)
                if msg != '': 
                    sock_tcp.send(msg.encode(UNICODE))
            except:
                msg = '/q'
    except:
        print(f'\nErro no UserInteraction...{sys.exc_info()[0]}')  
        exit() 
    closeSocket(sock_tcp)

# ============================================================================================================
