
import sys

def bar_progress (headers, data):
    dados_recebidos = 0
    content_length = 0
    # procuro no header a posição inicial do 'content_length' que vai me informar o tamanho da imagem + posição final
    dados_recebidos += len(data)
    inicio_length = headers.find(b'Content-Length:')
    if inicio_length != -1:
        final_length = headers.find(b'\r\n', inicio_length)
        # pego apenas a variavel do tamanho e transformo em inteiro (+16 corresponde ao nome 'content_length: ')
        content_length = int(headers[inicio_length+16:final_length])
        # printando na tela usando Dtdout.write (para escrever print sob print)
        sys.stdout.write(f'\rBytes baixados: {dados_recebidos} / {content_length} bytes')
        # flush para criar um buffer dos prints e ter sensação de carregamento
        sys.stdout.flush()
    return dados_recebidos, content_length