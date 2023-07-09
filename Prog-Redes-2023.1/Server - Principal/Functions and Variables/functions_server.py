import socket

def connection():
    ...


def cliInteraction(sock_client, info_client, clients_connected):
    msg = b'' # definindo uma mensagem binária
    while msg != b'/q': 
        try:
            msg = sock_client.recv(512)    
            broadCast (msg, info_client)
        except:
            msg = b'/q'
    print(clients_connected)
    del clients_connected[info_client[1]]
    print(clients_connected)
    sock_client.close()

def broadCast(msg, addrSource):
    msg = f"{addrSource} -> {msg.decode('utf-8')}"
    print (msg)
    for sockConn, addr in clients_connected:
        if addr != addrSource:
            sockConn.send(msg.encode('utf-8'))