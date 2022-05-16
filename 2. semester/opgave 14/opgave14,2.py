import threading
import time

def func(name):
    for n in range(500):
        print(name, end="")
        time.sleep(0.01)

if __name__ == "__main__":
    t1 = threading.Thread(target = func, args = ("T"))
    t2 = threading.Thread(target = func, args = ("M"))
    t3 = threading.Thread(target = func, args = ("Q"))

t1.start()
t1.join()
t2.start()
t2.join()
t3.start()