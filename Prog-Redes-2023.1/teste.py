import os, subprocess, platform

dir_atual = os.path.dirname(os.path.abspath(__file__))  # pegando a pasta atual
dir_arq =  os.path.abspath(__file__)
dir_temp = dir_atual + "\\Server-Principal"
system = platform.system()
print(system)

pid = 'python'
process = subprocess.run(['Powershell', 'Get-Process', '-Name', pid], capture_output=True, text=True).stdout.strip()

print(process)



arq = os.listdir(dir_atual + '\\pasta')
for x in arq:
    print(x)


'''








proc = subprocess.check_output(['tasklist', '/NH', '/FI', f'PID eq {pid}'])
print(proc)'''
'''if subprocess.run(['Powershell', 'Get-Process', '-Id', pid], capture_output=True, text=True).stdout.strip() != '':
    print('o1')
else:
    print('a')'''
'''def VERIFICATION_PID(pid):
    process = None

    if system == 'Windows':
        process = subprocess.run(['Powershell', 'Get-Process', '-Id', pid], capture_output=True, text=True).stdout.strip()
        print(process)
        print('o')
    elif system == 'linux':
        process = subprocess.run(['ps', '-p', pid], capture_output=True, text=True).stdout.strip()
        print('a')
    if process:
        print('oa')
        return True
    else:
        print('s')
        return False

VERIFICATION_PID(pid)'''

'''pid_file = dir_atual + '\\pid.temp'

with open(pid_file, 'r') as file:
    pid = int(file.readline().strip())
    print(type(pid))
    print(pid)'''