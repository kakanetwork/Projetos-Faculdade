
def PRINT_DIV(dados):
    print('\n'+'-'*100)
    print(dados)
    print('-'*100)

def COMAND_SPLIT(msg):
    try:
        msg_split = msg.split(':')
    except:
        print(f'\nErro no Split do Comand...{sys.exc_info()[0]}')  
        exit() 
    return msg_split