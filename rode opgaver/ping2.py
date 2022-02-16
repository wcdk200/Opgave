import os

hhmm = []
run = 0

while run <= 2:
    def myping(host):
        global hhmm
        global run
        response = os.system("ping -c 1 " + host)
        if response == 0:
            run = run + 1
            hhmm.append(myping)
            print(response)
            return True
        else:
            return False
    print(hhmm)    
    print(myping("8.8.8.8"))
      
#print(myping("8.8.8.8"))