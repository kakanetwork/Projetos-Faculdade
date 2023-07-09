import socket

def connection():
    ...


def cliInteraction(sockConn, addr):
    msg = b'' # definindo uma mensagem binária
    while msg != b'/q': 
        try:
            msg = sockConn.recv(512)    
            broadCast (msg, addr)
        except:
            msg = b'!q'
    del clients_connected[sockConn]
    sockConn.close()

def broadCast(msg, addrSource):
    msg = f"{addrSource} -> {msg.decode('utf-8')}"
    print (msg)
    for sockConn, addr in clients_connected:
        if addr != addrSource:
            sockConn.send(msg.encode('utf-8'))