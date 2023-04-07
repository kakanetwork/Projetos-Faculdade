
import os, platform, sys

def auto_clear(ativador):
    if ativador == True:
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

def dir_atual(ativador):
    if ativador == True:
      dir = os.path.dirname(os.path.abspath(__file__)) 
    return dir

def new_dir(nome):
    try:
        os.mkdir(nome)
    except FileExistsError:
        print(f'A Pasta ({nome}) já foi criada!\n')
    except:
        print(f'Erro na criação da pasta {nome}......: {sys.exc_info()[0]}\n')
        sys.exit()

def read_one_file(dir_arquivo, type1, separador):
    dados_lidos = list()
    leitura = False
    arquivo = None
    try:
        arquivo = open(dir_arquivo, 'r', encoding='utf-8')
        for leitura_linha in arquivo:
            leitura_linha = leitura_linha.rstrip('\n').split(separador)
            dados_lidos.append(leitura_linha)
        leitura = True
    except FileNotFoundError:
        print(f"Arquivo '{dir_arquivo}' não encontrado.\n")
    except PermissionError:
        print(f"Sem permissão para ler o arquivo '{dir_arquivo}'.\n")
    except:
        print(f"Ocorreu um erro inesperado ao ler o arquivo.......: {sys.exc_info()[0]}\n")
    finally:
        if arquivo is not None:
            arquivo.close()
        if leitura:
            print(f'Arquivo lido com sucesso...{dir_arquivo[:-1]}')      
    dados_lidos = type1(dados_lidos)
    return dados_lidos

# informe o diretorio onde tá todos arquivos, e o tipo que quer de OUTPUT
def read_all_files(dir_atual, type):
    try: 
        list_name_arq = tuple(os.listdir(dir_atual))
    except:
        print(f'Erro na localização do diretório (serie_historica_anp)......: {sys.exc_info()[0]}\n')
        sys.exit()
    conteudos = type()
    for filename in list_name_arq:
        print(f'Lendo arquivo: {filename}', end ='\n')
        try:
            arquivo = open(dir_atual + f'\\{filename}', 'r', encoding='utf-8')
            conteudo = arquivo.read()
            conteudos[filename] = conteudo
            arquivo.close()
        except FileNotFoundError:
            print(f"Arquivo '{filename}' não foi encontrado.\n")
        except PermissionError:
            print(f"Sem permissão para ler o arquivo '{filename}'.\n")
        except:
            print(f"Ocorreu um erro ao ler o arquivo.......: {sys.exc_info()[0]}\n")  
    return conteudos

def save_file_2(arquivo, dir2):
    try:
        file_name = input('Digite o nome do arquivo: ')
        file_path = os.path.join(dir2, file_name)
        with open(file_path, 'w') as file:
            for linha in arquivo:
                linha = [el if el is not None else "None" for el in linha]
                linha = [el.replace('""', '"vazio"') if isinstance(el, str) else el for el in linha]
                linha = str(linha).strip('[]').replace("'", "")
                file.write(linha + '\n\n')
            print(f'Variável salva com sucesso em {file_path}.')
    except PermissionError:
        print(f"Sem permissão para salvar o arquivo em '{dir2}'.")
    except Exception as e:
        print(f"Erro na escrita......: {e}")


def save_file(arquivo, dir2):
    try:
        file_name = input('Digite o nome do arquivo: ')
        file_path = os.path.join(dir2, file_name)
        with open(file_path, 'w') as file:
            for linha in arquivo:
                if linha is None:
                    linha = 'vazio'
                file.write(str(linha) + '\n')
            print(f'Variável salva com sucesso em {file_path}.')
    except PermissionError:
        print(f"Sem permissão para salvar o arquivo em '{dir2}'.")
    except:
        print(f"Erro na escrita......: {sys.exc_info()[0]}\n'")