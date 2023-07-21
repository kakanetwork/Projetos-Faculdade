import socket, threading, os, sys, subprocess, platform

dir_atual = os.path.dirname(os.path.abspath(__file__))  # pegando a pasta atual
dir_arq =  os.path.abspath(__file__)
system = platform.system()
dir_temp = dir_atual + "\\pid.temp"

# ============================================================================================================

''' VERIFICAÇÃO SE TODOS OS ARQUIVOS/PASTAS DE FUNÇÕES ESTÃO PRESENTES '''

def VERIFICATION_FUNCTIONS():
    dir_past = dir_atual + '\\Functions-and-Variables'
    sys.path.append(dir_past) # adicionando a pasta de funções na config de pesquisa de funções do sistema
    name_arqs = [
        'functions_bot.py',
        'functions_client.py',
        'functions_others.py',
        'functions_server.py',
        'functions_download.py',
        'variables.py']
    try:
        functions_arq = os.listdir(dir_past) # listando arquivos da pasta onde está as funções para verificar se todos os arquivos necessários estão lá
        for arquivos in name_arqs: 
            if arquivos not in functions_arq: # vendo qual o arquivo que falta
                print(f'\nO Arquivo "{arquivos}" não está presente dentro da pasta "Functions and Variables" faça o download dele!\n')
                sys.exit()
    except SystemExit:
        sys.exit()
    except FileNotFoundError: # para caso a pasta não exista
        print('\nA pasta "Functions and Variables" não foi encontrada, faça o download dela [com todas suas dependencias]!\n')
        sys.exit()
    except:
        print(f'\nErro na Verificação dos arquivos da Pasta de Funções...{sys.exc_info()[0]}')  
        sys.exit() 

VERIFICATION_FUNCTIONS()

# ============================================================================================================

def START_SERVER():
    try: 

        ''' CRIAÇÃO THREAD BOT / CRIAÇÃO DO SERVER / CRIAÇÃO DE PASTA'''

        clients_connected = dict() # lista de clientes conectados (IP:PORTA)
        sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # conexão IPV4/TCP
        sock_tcp.bind((SERVER, PORT)) # atribuindo Porta e Local
        CREATE_PAST(dir_atual + '\\server_files') # criando pasta onde sera guardado arquivos do server
        PRINT_DIV(f'Servidor: {SERVER} / {PORT}')
        thread_bot = threading.Thread(target=START_BOT, args=(clients_connected,)) # adicionando a thread do bot (pois sem ela, eu não consegueria rodar o server e o bot ao mesmo tempo)
        thread_bot.start() # iniciando a thread do bot
        sock_tcp.listen() # deixando indefinido quantidade máxima de conexões

    # ============================================================================================================

        ''' CONEXÃO DE CLIENTES / NOTIFICAÇÃO BOT / THREAD CLIENTE ''' 

        while True: 
            try:
                sock_client, info_client = sock_tcp.accept() # aceitando clientes 
                msg_connected = f"O Cliente de IP: {info_client[0]} | Na Porta: {info_client[1]}\nFoi conectado com sucesso!"
                PRINT_DIV(msg_connected) # printando o cliente conectado
                NOTIFICATION_BOT(msg_connected) # enviando mensagem para o bot do cliente que se conectou
                clients_connected[info_client[1]] = [info_client[0], sock_client] # adicionando o cliente ao dicionario de clientes conectados (PORTA:IP,SOCKET)
                thread_client = threading.Thread(target=CLIENT_INTERACTION, args=(sock_client, info_client, clients_connected, dir_atual)) # adicionando uma thread para cada cliente
                thread_client.start() # iniciando a thread

    # ============================================================================================================

            except:
                print(f'\nErro na Inicialização da Thread...{sys.exc_info()[0]}')  
                sys.exit() 
                
    except OSError as e: # exceção para quando a porta do servidor atual estiver ocupada
        if e.errno == 98:
            print('\nA porta atual do servidor se encontra ocupada\n')
            sys.exit()
    except SystemExit:
        ...
    except:
        print(f'\nErro na Inicialização do Server...{sys.exc_info()}')  
        sys.exit() 

# ============================================================================================================

from variables import SERVER, PORT
from functions_server import CLIENT_INTERACTION
from functions_others import PRINT_DIV, CREATE_PAST, SEARCH_FILES
from functions_bot import START_BOT, NOTIFICATION_BOT


START_SERVER()



'''def PROCESS_RUNNER():
    process_args = ["pythonw", "server.py"] 
    subprocess.Popen(process_args) 
    with open(pid_file, "w") as file:
        file.write(str(os.getpid()))
    sys.exit()    

def VERIFICATION_PID(pid):
    if system == 'windows':
        process = subprocess.run(['Powershell', 'Get-Process', '-Id', pid], capture_output=True, text=True).stdout.strip()
    elif system == 'linux':
        process = subprocess.run(['ps', '-p', '-Id', pid], capture_output=True, text=True).stdout.strip()
    if process:
        print(f'O Server já está sendo rodado em 2° Plano com o PID: {pid}')
        sys.exit()
    else:
        PROCESS_RUNNER()

def START():
    if os.path.isfile('pid.temp'):
        with open(dir_temp, 'r') as arquive:
            pid = arquive.readline().strip()
        VERIFICATION_PID(pid)

    else:
        # QUESTIONAR: O PROCESSO QUANDO É INICIADO ELE FICA COM NOME DO EXECUTOR "PYTHONW"
        # UMA FORMA DE CONTORNAR É USAR A LIB WIN32 PARA ALTERAR O NOME, MAS SÓ FUNCIONA NO WINDOWS
        # USAR O SUBPROCESS PARA PROCURAR NO SUBPROCESSO
        # PROCURAR O PROCESSO PELO NOme
        ...


'''



'''
if len(sys.argv) > 1: # verificando se passou +1 argumento
    arg = sys.argv[1] # pegando o primeiro argumento
    if arg == "/start": # verificando se foi /start
        temp = SEARCH_FILES(dir_temp, 'pid.temp') # utilizando função para varrer pasta e verificar se o arquivo existe
        if temp == True: # existindo a pasta e arquivo
            with open(pid_file, 'r') as file: # ele abre o arquivo em modo leitura
                pid = str(file.readline().strip()) # ler somente a primeira linha, tirando os espaços e transformando em string
            if system == "Windows": # verificando se o sistema é windows
                # no IF abaixo, faço a busca pelo processo de acordo com o PID (capture_output = retornar captura, e text = retornar formatado) e se diferente de vazio
                if subprocess.run(['Powershell', 'Get-Process', '-Id', pid], capture_output=True, text=True).stdout.strip() != '':
                    print('O SERVER JÁ ESTÁ ONLINE')
                else: 
                    process_args = ["pythonw", "server.py"] # no caso não existindo processo com o PID, ele vai executar o código
                    subprocess.Popen(process_args) 
                    CREATE_PAST(dir_temp)
                    with open(pid_file, "w") as file:
                        file.write(str(os.getpid()))
                    sys.exit()
            
    elif arg == "/stop":
        ...
    elif arg == "/?":
        ...
    else:
        ...'''

