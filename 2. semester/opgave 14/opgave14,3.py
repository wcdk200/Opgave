import threading
import time

def func(name):
    for n in range(500):
        print(name, end="")
        time.sleep(0.1)

def func2(name):
    for n in range(500):
        print(name, end="")
        time.sleep(1)


if __name__ == "__main__":
    tA = threading.Thread(target = func, args = ("A"))
    tB = threading.Thread(target = func2, args = ("B"))

tA.start()
tB.start()