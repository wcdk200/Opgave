import platform
import subprocess

run = 0

while run <= 1:
    def myping(host):
        global run
        parameter = '-n' if platform.system().lower()=='windows' else '-c'

        command = ['ping', parameter, '1', host]
        response = subprocess.call(command)

        if response == 0:
            run = run + 1
            return True
        else:
            return False

    print(myping("8.8.8.8"))

