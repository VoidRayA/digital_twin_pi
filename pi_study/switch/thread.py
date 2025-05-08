from threading import Thread
from time import sleep

def fx1():
    for i in range(10):
        print(f"fx1 - {i}")
        sleep(1)
def fx2():
    for i in range(10):
        print(f"fx2 - {i}")
        sleep(1)

if __name__ == "__main__":
    thread1 = Thread(target=fx1, daemon=True)
    thread2 = Thread(target=fx2, daemon=True)
    thread1.start()
    thread2.start()
    
    sleep(2)
    
    print("Main Exit")