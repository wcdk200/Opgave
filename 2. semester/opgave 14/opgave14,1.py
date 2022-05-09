import threading
import time

def func(name):
    for n in range(500):
        print(name, end="")
        time.sleep(0.0)

if __name__ == "__main__":
    t1 = threading.Thread(target = func, args = ("T"))
    t2 = threading.Thread(target = func, args = ("M"))

t1.start()
t2.start()