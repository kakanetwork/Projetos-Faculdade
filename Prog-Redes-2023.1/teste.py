import os, subprocess

dir_atual = os.path.dirname(os.path.abspath(__file__))  # pegando a pasta atual
dir_arq =  os.path.abspath(__file__)
dir_temp = dir_atual + "\\Server-Principal"
'''

proc = subprocess.check_output(['tasklist', '/NH', '/FI', f'PID eq {pid}'])
print(proc)'''
pid = '58552'
processo = subprocess.run(['Powershell', 'Get-Process', '-Id', pid], capture_output=True, text=True).stdout.strip()

print(processo)


'''pid_file = dir_atual + '\\pid.temp'

with open(pid_file, 'r') as file:
    pid = int(file.readline().strip())
    print(type(pid))
    print(pid)'''