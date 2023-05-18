import socket

host  = input('\nInforme o nome do HOST ou URL do site: ')
port  = 80

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((host , port))

requisicao = f'HEAD / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\n\r\n'
tcp_socket.sendall(requisicao.encode('utf-8'))

print('-'*100)
print(str(tcp_socket.recv(1024), 'utf-8'))
print('-'*100)

tcp_socket.close()