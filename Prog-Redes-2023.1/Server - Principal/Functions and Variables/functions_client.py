import socket

def closeSocket():
    try:
        sock.close()
    except:
        None

def servInteraction():
    msg = b' '
    while msg != b'':
        try:
            msg = sock.recv(512)
            print ("\n"+msg.decode('utf-8')+"\n"+PROMPT)
        except:
            msg = b''
    closeSocket()

def userInteraction():
    msg = ''
    while msg != '/q':
        try:
            msg = input(PROMPT)
            if msg != '': sock.send(msg.encode('utf-8'))
        except:
            msg = '/q'
    closeSocket()

