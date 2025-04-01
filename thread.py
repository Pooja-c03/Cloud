import threading
import os

def info():
    print(f"Process ID: {os.getpid()}, Thread ID: {threading.get_ident()}, Thread Name: {threading.current_thread().name}")

if __name__ == "__main__":
    t1 = threading.Thread(target=info, name="Thread1")
    t2 = threading.Thread(target=info, name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Process ID : {os.getpid()}, Thread ID: {threading.get_ident()}, Thread Name: {threading.current_thread().name}")