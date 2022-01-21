
import subprocess
import time

process = []

while True:
    action = input('Выберите действие: q - выход , s - запустить сервер и клиенты, x - закрыть все окна:')

    if action == 'q':
        break
    elif action == 's':

        #start server
        process.append(subprocess.Popen(f'xfce4-terminal --execute python3 /home/python/python-gb-client-server/python-gb-client-server/task_l3_1/server.py', shell=True))

        # Запускаем клиентов:
        time.sleep(0.5)
        process.append(subprocess.Popen(f'xfce4-terminal --execute python3 /home/python/python-gb-client-server/python-gb-client-server/task_l3_1/client.py', shell=True))

            

    elif action == 'x':
        while process:
            victim = process.pop()
            victim.kill()
            victim.terminate()
