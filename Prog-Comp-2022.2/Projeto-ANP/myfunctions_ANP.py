import sys

def leitura_arq(lista_arq, dir_anp):
    dados_lidos = list()
    for filename in lista_arq: 
        print(f'Lendo arquivo: {filename}', end ='\n')
        try:
            arquivo_open = open(dir_anp + f'\\{filename}', 'r', encoding='utf-8')
        except:
            print(f'Erro na leitura......: {sys.exc_info()[0]}')
        else:
            linha = arquivo_open.readline()
            while True:
                linha = arquivo_open.readline()[:-1]
                if not linha: break
                linha = linha.split(';')
                dados_lidos.append([linha[0], linha[1], linha[10], linha[11], float(linha[12].replace(',','.')), linha[15]])  
            bool = True
            arquivo_open.close()
        finally:
            if bool: print(f'Arquivo lido: {filename}\n')
    dados_lidos = tuple(dados_lidos)
    return dados_lidos