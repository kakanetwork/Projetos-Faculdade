import pyfiglet

def ASCII_ART(frase):
    try:
        arte = pyfiglet.figlet_format(frase)
        print(arte, end='')
    except: pass
