import socket, sys, logging
from functions_others import *
from variables import *
from functions_download import *

loggerServer  = logging.getLogger('Server')
loggerDebug  = logging.getLogger('Debug')

# ============================================================================================================

''' FUNÇÃO PARA REALIZAR O CHAT ENTRE CLIENTES ESPECIFICOS  '''

def CHAT(comand=None, clients=None, info_client=None, sock=None, **kwargs): 
    try:
        ip_destination = comand[1] # guardando o ip de destino da mensagem
        port = comand[2] # guardando a porta de destino
        bool = False
        for chave, valor in clients.items(): # dando um for na lista de clientes
            port_envio = str(chave) # Armazenamento Temporário 
            ip_envio = valor[0] # Armazenamento Temporário 
            sock_envio = valor[1] # pegando o socket do cliente destino 
            if ip_destination == ip_envio and port == port_envio: # verificando se o ip/porta (ou seja cliente) está conectado ao servidor
                msg_chat = f"\nO Cliente: {info_client[0]}:{info_client[1]} lhe enviou uma mensagem!\nMensagem >> {comand[3]}\n" # formatação de mensagem
                MESSAGE_CLIENT(sock_envio, msg_chat) # realizando o envio para o socket do cliente destino
                bool = True
                break
        if not bool:
            msg_erro = f"\nO Cliente informado para encaminhar a mensagem não está conectado ao Servidor!\n"
            MESSAGE_CLIENT(sock, msg_erro)
    except IndexError: # para caso não seja repassado todos os argumentos de /m
        msg_erro = f"\nInforme todos os argumentos/parametros necessários para essa opção!\n"
        MESSAGE_CLIENT(sock, msg_erro)
        return
    except:
        loggerServer.error(f'Erro no Chat...{sys.exc_info()[0]}')  
        exit() 
            
# ============================================================================================================

''' FUNÇÃO PARA REALIZAR A LISTAGEM DE CLIENTES CONECTADOS AO SERVIDOR '''

def LIST_CLIENTS(clients=None, sock=None, **kwargs):
    try: 
        msg_list = "\nOs Clientes conectados ao Servidor são:\n\n" # formatando mensagem 
        num = 0
        for chave, valor in clients.items():  # faço um for para pegar cada cliente conectado e enviar 
            ip = valor[0] # Armazenamento Temporário 
            num+=1 # formatação numeração cliente
            msg_list += f"\nCLIENTE {num}\nIP: {ip}\nPORT: {chave}\n\n" # formatação listagem clientes (lembrando que chave=porta e valor[0]=ip)
        MESSAGE_CLIENT(sock, msg_list) # enviando mensagens 
    except:
        loggerServer.error(f'Erro no momento de Listar os Clientes Conectados...{sys.exc_info()[0]}')  
        exit() 

# ============================================================================================================

''' FUNÇÃO PARA ENVIAR MENSAGEM EM MODO BROADCAST (P/ TODOS CLIENTES, EXCETO QUEM PEDIU) '''

def BROADCAST (clients=None, info_client=None, sock=None, comand=None, **kwargs):
    try:
        msg = comand[1]
        if msg: # para caso não tenha digitado nada apenas /b:
            msg_broadcast = f"\nO Cliente: {info_client[0]} : {info_client[1]} Enviou uma mensagem para Todos!\nMensagem >> {comand[1]}\n" # formatação de mensagem
            for chave, valor in clients.items(): # realizando o for para mandar p/ todos os clientes
                port_envio = chave # Armazenamento Temporário 
                ip_envio = valor[0] # Armazenamento Temporário 
                if port_envio != info_client[1]: # pegando sock de todos, exceto do cliente que pediu
                    sock_broadcast = valor[1] # Armazenamento Temporário 
                    MESSAGE_CLIENT(sock_broadcast, msg_broadcast) # enviando mensagem
        else: # para caso cliente envie apenas vazio, peço para digitar algo
            msg_erro = f"\nDigite algo!\n"
            MESSAGE_CLIENT(sock, msg_erro)
    except IndexError: # para caso não seja repassado todos os argumentos de /b
        msg_erro = f"\nInforme todos os argumentos/parametros necessários para essa opção\n"
        MESSAGE_CLIENT(sock, msg_erro)
    except:
        loggerServer.error(f'Erro no momento de enviar o Broadcast...{sys.exc_info()[0]}')  
        exit()                 

# ============================================================================================================

''' FUNÇÃO PARA ENVIAR AO CLIENTE O SEU HISTÓRICO DE COMANDOS '''

def HISTORY(history=None, sock=None, **kwargs):
    try:
        msg_history = f"\nEsse é o seu histórico de comandos:\n\n" # formatação mensagem
        num = 0
        for comands in history: # pegando cada comando do histórico
            num += 1 
            msg_history += f"    {num} {comands}\n" # formatando linha:comando
        MESSAGE_CLIENT(sock, msg_history)
    except:
        loggerServer.error(f'Erro no momento de enviar o Histórico de Comandos...{sys.exc_info()[0]}')  
        exit()  

# ============================================================================================================

''' FUNÇÃO QUE LISTA AS OPÇÕES DISPONIVEIS PARA O CLIENTE '''

def HELP(sock=None, **kwargs):
    try:
        # Criando descrição de cada comando
        descriptive_options = {
        '/l': 'Listar clientes conectados',
        '/m:ip:porta:mensagem': 'Enviar mensagem para cliente especifíco [Informe IP:PORTA do scliente]',
        '/b:mensagem': 'Enviar mensagem em Broadcast [Informe mensagem]',
        '/h': 'Lista o seu histórico de comandos',
        '/f': 'Lista os arquivos disponiveis para download local',
        '/d:arquivo': 'Faz o download de um arquivo do servidor [Informe nome do arquivo]',
        '/u:arquivo': 'Faz upload do arquivo para o Server',
        '/w:url' : 'Faz o download do arquivo de uma URL no banco do servidor [Informe uma URL]',
        '/?': 'Lista as opções disponiveis',
        '/q': 'Desconectar do Servidor'
        }
        msg_help = f"\nSegue abaixo as Opções disponiveis neste servidor:\n\n" # formatação mensagem
        for comando, descrição in descriptive_options.items(): # listando por meio do FOR comando por comando 
            msg_help += f"  {comando} -> {descrição}\n" # formatação mensagem'
        MESSAGE_CLIENT(sock, msg_help)
    except:
        loggerServer.error(f'Erro no momento de listar as Opções...{sys.exc_info()[0]}')  
        exit()  

# ============================================================================================================

''' FUNÇÃO PARA LISTAR OS ARQUIVOS DISPONIVEIS PARA DOWNLOAD '''

def LIST_FILES(sock=None, dir=None, **kwargs):
    try:
        dir_arq = dir + '\\server_files'
        past_arquives = os.listdir(dir_arq) # faço a listagem de arquivos na pasta referente
        msg_list = f"\nOs arquivos disponiveis para download são:\n" # formatação da mensagem
        num = 0 
        for arquives in past_arquives: # percorro cada arquivo da pasta
            num += 1 
            size = os.path.getsize(dir_arq + f'\\{arquives}')
            msg_list += f"       {num}° Name: {arquives} | Size: {size} Bytes\n" # formatação da mensagem
        MESSAGE_CLIENT(sock, msg_list)
    except:
        loggerServer.error(f'Erro no momento de listar os Arquivos para Download...{sys.exc_info()[0]}')  
        exit()  

# ============================================================================================================

def DOWNLOAD_RSS():
    # EM DESENVOLVIMENTO...
    ...



# ============================================================================================================

''' FUNÇÃO PARA REALIZAR O RECEBIMENTO DO UPLOAD DO CLIENTE '''

def UPLOAD_RECV(comand=None, sock=None, dir=None, **kwargs):
    size = int(comand[1]) # pegando o tamanho enviado antecipadamente 
    name = comand[2] # pegando o nome enviado antecipadamente 
    try:
        local_arquive = dir + f'\\server_files\\{name}' # definindo o local de save
        with open(local_arquive, 'wb') as arquivo: # abrindo o arquivo em "Wb" -> Leitura Binária
            msg_upload = f'\nGravando Arquivo no Servidor\nNome: {name}\nTamanho: {size} bytes\n'
            MESSAGE_CLIENT(sock, msg_upload) # enviando mensagem para o cliente 
            bytes_recebidos = 0 
            pct = 1
            while True: 
                data_arquive = sock.recv(BUFFER) # Recebendo o conteúdo 
                if not data_arquive: break
                arquivo.write(data_arquive) # escrevendo 
                bytes_recebidos += len(data_arquive) # adicionando cada pacote de bytes aos bytes recebidos
                msg_upload = f'Pacote ({pct}) - Dados: {bytes_recebidos}/{size} bytes\n' # informando o processamento
                MESSAGE_CLIENT(sock, msg_upload)
                if bytes_recebidos >= size: break # após os bytes recebidos forem iguais ou excederem o tamanho enviado antecipadamente, ele encerra.
                pct += 1
        msg_upload = f'\n\nO Upload do arquivo {name} foi finalizado!\n' # informando que o Upload foi feito com sucesso
        MESSAGE_CLIENT(sock, msg_upload)
    except FileNotFoundError: # erro já tratado no lado cliente, apenas para evitar logs 
        ...
    except:
        loggerServer.error(f'Erro no recebimento dos dados pelo Upload [Lado servidor]...{sys.exc_info()[0]}')

# ============================================================================================================

''' FUNÇÃO PARA REALIZAR O DOWNLOAD DE QUALQUER ARQUIVO VIA URL '''

def DOWNLOAD_URL(sock=None, msg=None, dir=None, **kwargs):
    try:
        url_brute = str(msg[3:]) # pegando a URL do comando (/m:URL) apartir da 3° posição
        try:
            hostname, localarquive, arquivename, protocol = SPLIT_URL(url_brute) # Realizando split da URL para pegar parametros especificos
        except:
            msg_erro = '\nInforme a URL corretamente... (tente novamente)!\n' # Realizo tratamento fora da função [motivo: debug facilitado]
            MESSAGE_CLIENT(sock, msg_erro)
            return
        try:        
            # Realizando conexão HTTP/HTTPS a depender da URL
            if protocol =='https': 
                socket_conexão = SOCKET_HTTPS(localarquive, hostname)  
            elif protocol =='http':
                socket_conexão = SOCKET_HTTP(localarquive, hostname)   
            else:
                msg_erro = '\nProtocolo Não suportado... Em Desenvolvimento...\n' 
                MESSAGE_CLIENT(sock, msg_erro)
        except:
            msg_erro = '\nA Requisição não teve sucesso, verifique a URL... (tente novamente)!\n'
            MESSAGE_CLIENT(sock, msg_erro)
            return
        # Separei as funções para a DOWNLOAD_WEB realizar o bruto [motivo: debug facilitado/redução de código/modulação]
        arquivo_dados, content_type = DOWNLOAD_WEB(socket_conexão, sock) # me retorna o arquivo/extensão dele
        nome_arquivo = f'{arquivename}.{content_type}' # definindo o nome do arquivo com o nome retirado da URL + sua extensão real 
        diretorio_arquivo = dir + f'\\server_files\\{nome_arquivo}' # definindo local de save
        with open(diretorio_arquivo, 'wb') as arquivo: # gravando o arquivo
            arquivo.write(arquivo_dados)
    except IndexError: # caso do cliente não passar todos os argumentos necessários
        msg_erro = "\nInforme todos os argumentos/parametros necessários para essa opção\n"
        MESSAGE_CLIENT(sock, msg_erro)
    except:
        loggerServer.error(f'Erro no momento de fazer o Download da URL...{sys.exc_info()[0]}')  
        exit()  

# ============================================================================================================

''' FUNÇÃO PARA REALIZAR O DOWNLOAD DE UM ARQUIVO LOCAL DO SERVIDOR '''

def DOWNLOAD_SEND(comand=None, dir=None, sock=None, **kwargs):
    try:
        dir_arq = dir + '\\server_files' # montando diretorio de onde tá os arquivos lado server
        nome_arquivo = dir_arq + f'\\{comand[1]}' # pegando o nome do arquivo fornecido e montando caminho absoluto
        if not os.path.exists(nome_arquivo): # verificando se o arquivo fornecido existe
            msg_local = f'\nO Arquivo que você pediu "{comand[1]}" não existe no servidor!\nDê /f para consultar os arquivos existentes\n'
            MESSAGE_CLIENT(sock, msg_local) # se não existir ele informa que não existe
            return
        size_arq = os.path.getsize(nome_arquivo) # existindo ele pega o tamanho do arquivo
        msg_local = f'/d:{size_arq}:{comand[1]}' # e faço o envio do comando, nome e tamanho do arquivo 
        MESSAGE_CLIENT(sock, msg_local)
        with open(nome_arquivo, 'rb') as arquive: # lendo o arquivo
            while True:
                dados_img = arquive.read(BUFFER) 
                if not dados_img:
                    break
                sock.send(dados_img) # enviando o arquivo
    except FileNotFoundError:
        pass 
    except IndexError: # para caso não seja repassado todos os argumentos de /d
        msg_erro = f"\nInforme todos os argumentos/parametros necessários para essa opção\n"
        MESSAGE_CLIENT(sock, msg_erro)
    except:
        loggerServer.error(f'Erro no momento fazer o Envio do Download Local...{sys.exc_info()[0]}')  

# ============================================================================================================

''' FUNÇÃO QUE REALIZA A INTERAÇÃO DO CLIENTE (DEFINE A FUNÇÃO A SER CHAMADA DE ACORDO COM O PEDIDO DO CLIENTE) '''

def CLIENT_INTERACTION(sock_client, info_client, clients_connected, dir_atual):
    try:
        history_client = list()
        options = { # dicionário com todas as opções para o cliente (sendo o valor a função ser chamada)
            '/l': LIST_CLIENTS,
            '/m': CHAT,
            '/b': BROADCAST,
            '/h': HISTORY,
            '/?': HELP,
            '/f': LIST_FILES,
            '/d': DOWNLOAD_SEND,
            '/u': UPLOAD_RECV,
            '/w': DOWNLOAD_URL,
            '/rss': DOWNLOAD_RSS}
        options_choice = set(options.keys()) # usado para verificar se o comando pertence ao dicionário 
        while True: # continuar ouvindo o cliente a menos que ele digite /q 
            msg = sock_client.recv(BUFFER_SIZE01).decode(UNICODE) # recebendo mensagem do cliente
            history_client.append(msg) # histórico de comandos do cliente
            comand = COMAND_SPLIT(msg) # realizando split do comando do cliente 
            comand_prompt = comand[0].lower() # usando apenas para pegar o comando bruto "/x"
            if comand_prompt == '/q':
                loggerServer.info(f"O cliente {info_client[0]}:{info_client[1]} encerrou a conexao.")
                break
            if comand_prompt in options_choice:  # verificando se o comando está dentro das opções disponivéis 
                # ativando a função chamada (passando argumento depois)
                options[comand_prompt](clients=clients_connected, sock=sock_client, comand=comand, info_client=info_client, history=history_client, options=options, dir=dir_atual, msg=msg)
        del clients_connected[info_client[1]] # quando o cliente digitar /q ele exclui socket do cliente da lista de clientes ativos
        sock_client.close()
    except:
        loggerServer.critical(f'Erro na Interação do Cliente [pelo servidor]...{sys.exc_info()[0]}')  
        del clients_connected[info_client[1]] # caso o cliente seja desconectado por algum erro, ele apaga o cliente da lista de clientes ativos
        sock_client.close() 
        exit() 

# ============================================================================================================