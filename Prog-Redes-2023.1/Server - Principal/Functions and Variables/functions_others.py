import sys
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
        msg_split = msg.lower().split(':')
    except:
        print(f'\nErro no Split do Comand...{sys.exc_info()[0]}')  
        exit() 
    return msg_split

# ============================================================================================================

