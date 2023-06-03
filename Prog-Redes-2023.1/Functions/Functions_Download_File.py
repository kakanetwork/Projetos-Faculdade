import socket, ssl, sys, time
from Functions_Simple import content_length, content_type

"IMPORTANTE: ANTES DA EXECUÇÃO DO CÓDIGO FAÇA O DOWNLOAD DA PASTA (FUNCTIONS) ONDE CONTÉM AS FUNÇÕES PARA O FUNCIONAMENTO DESTE CÓDIGO!"

# -----------------------------------------------------------------------------------------------------------

def download_file(socket_conexão, buffer_size):
    print('\nBaixando o arquivo...')
    data_ret = b'' 
    dados_recebidos = 0
    try:
        content_length = -1
        start_time = time.time()   # iniciando contagem de tempo
        while True:     # recebendo a resposta 
            data = socket_conexão.recv(buffer_size)    # recebe a resposta em pedaços de Xbytes (x = buffer_size)
            if not data: 
                break
            data_ret += data
            dados_recebidos += len(data)    # joga na variavel o quanto de bytes já foram recebidos
            position  = data_ret.find('\r\n\r\n'.encode())
            headers   = data_ret[:position].decode('utf-8')   # pegando o cabeçalho 

            # -----------------------------------------------------------------------------------------------------------
            try:
                content_length = Functions_Simple.content_length(headers)    # função para capturar o content length no header
                print(f'\rBytes baixados: {dados_recebidos} / {content_length} bytes', end='')
            except: pass  # passando pois o content_length não é vital para o código
        if content_length == -1:
            print('Não foi possivel capturar o Content_Lenght...')  # criando um aviso para quando o content lenght não for pego 
        arquivo_dados = data_ret[position+4:]   # pegando os dados do arquivo
        Content_type = Functions_Simple.content_type(headers) # usando a função para pegar a extensão do arquivo pelo header
        print('\nDownload Concluído...\n')
        end_time = time.time() 
        tempo_total = end_time - start_time
        print(f'Tempo total: {tempo_total:.2f}s\n') # informando o tempo total de download

        # -----------------------------------------------------------------------------------------------------------
    except KeyboardInterrupt:
        print('\nVocê encerrou o programa com sucesso!\n')
        exit() 
    except:
        print(f'\nErro no recebimento dos dados...{sys.exc_info()[0]}')  
        exit()  
    socket_conexão.close() # fechando a conexão
    return headers, arquivo_dados, Content_type
# -----------------------------------------------------------------------------------------------------------