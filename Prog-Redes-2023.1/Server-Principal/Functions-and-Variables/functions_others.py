import sys, os
from variables import *

# ============================================================================================================

''' FUNÇÃO PARA REALIZAR PRINT ORGANIZADO '''

def PRINT_DIV(dados):
    print('\n'+'-'*100)
    print(dados)
    print('-'*100)

# ============================================================================================================

''' FUNÇÃO PARA REALIZAR SPLIT DO COMANDO DO CLIENTE '''

def COMAND_SPLIT(msg):
    try:
        msg_split = msg.split(':')
    except:
        print(f'\nErro no Split do Comand...{sys.exc_info()[0]}')  
        exit() 
    return msg_split

# ============================================================================================================

def CREATE_PAST(name):
    try:
        os.makedirs(name, exist_ok=True)
    except:
        print(f'\nErro na Criação da Pasta...{sys.exc_info()}')  
        exit()      

# ============================================================================================================

def SEARCH_FILES(dir, name):
    if os.path.exists(dir):
        list_files = os.listdir(dir)
        if name in list_files:
            return True
        else:
            return False
    else:
        return False

# ============================================================================================================

def VERIFICATION_PID():
    ...

# ============================================================================================================

def BUFFER_DIVISION(size):
    BUFFER_SIZE = size/4
    if BUFFER_SIZE < 512:
        BUFFER_SIZE = 512
    return BUFFER_SIZE