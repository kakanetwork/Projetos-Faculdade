import pyfiglet

def ascii_art(frase):
    arte = pyfiglet.figlet_format(frase)
    print(arte, end='')
    
