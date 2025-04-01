import threading
import time

def find_square(num):
    time.sleep(1)
    print(f"Square of {num}: {num**2}")

def find_cube(num):
    time.sleep(1)
    print(f"Cube of {num}: {num**3}")

if __name__ == "__main__":
    num = int(input("Enter the no: "))

    thread1 = threading.Thread(target=find_square, args=(num,))
    thread2 = threading.Thread(target=find_cube,args=(num,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Both threads completed execution")