import socket

def connection():
    ...


def CLIENT_INTERACTION(sock_client, info_client, clients_connected):
    msg = b'' # definindo uma mensagem binária
    while msg != b'/q': # o while 
        try:
            msg = sock_client.recv(512)    
            broadCast (msg, info_client)
        except:
            msg = b'/q'
    del clients_connected[info_client[1]]
    sock_client.close()

def broadCast(msg, addrSource):
    msg = f"{addrSource} -> {msg.decode('utf-8')}"
    print (msg)
    for sockConn, addr in clients_connected:
        if addr != addrSource:
            sockConn.send(msg.encode('utf-8'))