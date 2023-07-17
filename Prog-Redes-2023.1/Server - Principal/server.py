
import socket, threading, os, sys, platform, subprocess

'''def bg():
    comando = ["python", "server.pyw"]
    subprocess.Popen(comando, shell=True)

bg()'''

# TENTATIVA 2° PLANO

'''PORT = 5678

if platform.system() == 'Windows':
    print('oi')
    subprocess.Popen(['pythonw', __file__, str(PORT)], shell=True)  
    exit()
'''
# ============================================================================================================

''' VERIFICAÇÃO SE TODOS OS ARQUIVOS/PASTAS DE FUNÇÕES ESTÃO PRESENTES '''

dir_atual = os.path.dirname(os.path.abspath(__file__)) # pegando sua pasta atual
dir_past = dir_atual + '\\Functions and Variables'
name_arqs = ['functions_bot.py', 'functions_client.py', 'functions_others.py', 'functions_server.py', 'variables.py']

try:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\Functions and Variables') # adicionando a pasta de funções na config de pesquisa de funções do sistema
    functions_arq = os.listdir(dir_past) # listando arquivos da pasta onde está as funções para verificar se todos os arquivos necessários estão lá
    for arquivos in name_arqs: 
        if arquivos not in functions_arq: # vendo qual o arquivo que falta
            print(f'\nO Arquivo "{arquivos}" não está presente dentro da pasta "Functions and Variables",' +
            'faça o download dele para o funcionamento correto do código!\n')
            exit()
except FileNotFoundError: # para caso a pasta não exista
    print('\nA pasta "Functions and Variables" não foi encontrada, faça o download dela para o' 
    + 'funcionamento correto do código [com todas suas dependencias]!\n')
    sys.exit()
except:
    print(f'\nErro na Verificação dos arquivos da Pasta de Funções...{sys.exc_info()[0]}')  
    sys.exit() 

# ============================================================================================================

''' FUNÇÕES IMPORTADAS DOS ARQUIVOS '''


from variables import *
from functions_server import CLIENT_INTERACTION
from functions_others import PRINT_DIV
from functions_bot import *


# ============================================================================================================

try: 
    clients_connected = dict() # lista de clientes conectados (IP:PORTA)
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # conexão IPV4/TCP
    sock_tcp.bind((SERVER, PORT)) # atribuindo Porta e Local
    PRINT_DIV(f'Servidor: {SERVER} / {PORT}')
    thread_bot = threading.Thread(target=START_BOT, args=(clients_connected,)) # adicionando a thread do bot (pois sem ela, eu não consegueria rodar o server e o bot ao mesmo tempo)
    thread_bot.start() # iniciando a thread do bot
    sock_tcp.listen() # deixando indefinido quantidade máxima de conexões

# ============================================================================================================

    while True: 
        try:
            sock_client, info_client = sock_tcp.accept() # aceitando clientes 
            msg_connected = f"O Cliente de IP: {info_client[0]} | Na Porta: {info_client[1]}\nFoi conectado com sucesso!"
            PRINT_DIV(msg_connected) # printando o cliente conectado
            NOTIFICATION_BOT(msg_connected) # enviando mensagem para o bot do cliente que se conectou
            clients_connected[info_client[1]] = [info_client[0], sock_client] # adicionando o cliente ao dicionario de clientes conectados (PORTA:IP,SOCKET)
            thread_client = threading.Thread(target=CLIENT_INTERACTION, args=(sock_client, info_client, clients_connected)) # adicionando uma thread para cada cliente
            thread_client.start() # iniciando a thread

# ============================================================================================================

        except:
            print(f'\nErro na Inicialização da Thread...{sys.exc_info()[0]}')  
            sys.exit() 
except:
    print(f'\nErro na Inicialização do Server...{sys.exc_info()[0]}')  
    sys.exit() 
