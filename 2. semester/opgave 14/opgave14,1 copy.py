import threading
import time

def func(name):
    for n in range(500):
        print(name, end="")
        time.sleep(0.1)

if __name__ == "__main__":
    tA = threading.Thread(target = func, args = ("A"))
    tB = threading.Thread(target = func, args = ("B"))

tA.start()
tA.join()
tB.start()
tB.join()