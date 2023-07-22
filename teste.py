import os, subprocess, platform, sys, time

dir_atual = os.path.dirname(os.path.abspath(__file__))  # pegando a pasta atual
dir_arq =  os.path.abspath(__file__)
dir_temp = dir_atual + "\\pid.temp"
pid_file = dir

pid = 'pythonw'

process = subprocess.run(['Powershell', 'Get-Process', pid, '-IncludeUsername'], capture_output=True, text=True).stdout.strip()
if process:
    print('serviço já em execução')
else:
    comadno = "pythonw teste.py"
    processo = os.system(comadno)
    with open(dir_temp, "w") as file:
        file.write(str(os.getpid()))
