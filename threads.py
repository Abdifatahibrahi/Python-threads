import time
from threading import Thread


def ask_user():
    start = time.time()
    name = input("What is your name ? ")
    print(name)
    print(f"ask user: {time.time() - start}")


def complex_calculations():
    start = time.time()
    print("start calculating........")
    [x**2 for x in range(20000000)]
    print(f"complex calculation time: {time.time() - start}")



start = time.time()
ask_user()
complex_calculations()
print(f"single thread total time: {time.time() - start}")



start = time.time()
thread1 = Thread(target=complex_calculations)
thread2 = Thread(target=ask_user)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"two threads at the same time: {time.time() - start}")
