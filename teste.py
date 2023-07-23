import os
import sys
import time
import subprocess
import psutil

def is_process_running(process_name):
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
