import socket

def SERVER_TCP (HOST_SERVER, SOCKET_PORT, CONEXÕES):
    # Criação do socket (IPV4 / TCP)
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Vinculando ao host e porta 
    socket_server.bind((HOST_SERVER,SOCKET_PORT))
    # definindo quantas conexões ele ira atender
    socket_server.listen(CONEXÕES)
    return socket_server

def CLIENT_TCP (HOST_SERVER, SOCKET_PORT, MSG, CODE_PAGE):
    socket_client.connect((HOST_SERVER, SOCKET_PORT))  
    socket_client.send(MSG.encode(CODE_PAGE)) 
    return socket_client

def RECV (SOCKET_PEDIDO, BUFFER_SIZE, CODE_PAGE=None):
    dados = SOCKET_PEDIDO.recv(BUFFER_SIZE)
    if CODE_PAGE:
        dados = dados.CODE_PAGE(CODE_PAGE)
    return dados