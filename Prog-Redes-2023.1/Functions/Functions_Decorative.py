import pyfiglet

def ascii_art(frase):
    try:
        arte = pyfiglet.figlet_format(frase)
        print(arte, end='')
    except: pass
