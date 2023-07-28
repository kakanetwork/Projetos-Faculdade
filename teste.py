import os
import sys
import time
import subprocess
import psutil

dir_atual = os.path.dirname(os.path.abspath(__file__))  # pegando a pasta atual
dir_arq =  os.path.abspath(__file__) 
dir_pid = dir_atual + "\\pid.temp"
dir_logconf = dir_atual + "\\log.ini"
dir_log = dir_atual + "\\log.log"
dir_pastdownload = dir_atual + '\\server_files'


'''msg_log = "LISTAGEM LOG SERVIDOR\nDATA - LOGGER - TIPO - INFORMAÇÃO\n"
with open(dir_log, 'r') as arquive:
    msg_log += arquive.read()
print(msg_log)
'''

process = subprocess.Popen(["pythonw", "teste.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
print(process.pid)
time.sleep(100)
sys.exit()




'''def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

def main():
    # Coloque aqui o código que deseja executar em segundo plano.
    # Neste exemplo, estamos apenas esperando por 10 segundos.
    time.sleep(10)

def run_background_process():
    process_name = "pythonw.exe"
    script_name = os.path.basename(__file__)

    # Verifica se um processo com o mesmo nome já está em execução em segundo plano
    if is_process_running(process_name) and is_process_running(script_name):
        print(f"O processo '{script_name}' já está em execução em segundo plano.")
        sys.exit()

    # Executa o próprio script em segundo plano
    subprocess.Popen(['pythonw', script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Executa a função 'main' em segundo plano
    main()

if __name__ == "__main__":
    print("Agora irá rodar em segundo plano.")
    run_background_process()
'''