import threading
import time
import random

philosophers_number = 5
forks = [threading.Semaphore(1) for _ in range(philosophers_number)]

def philosopher(philosopher_id):
    while True:
        think(philosopher_id)
        get_fork(philosopher_id)
        eat(philosopher_id)
        drop_fork(philosopher_id)

def think(philosopher_id):
    print(f"Filósofo {philosopher_id} está pensando.")
    time.sleep(random.uniform(1, 3))

def get_fork(philosopher_id):
    fork_left = philosopher_id
    fork_right = (philosopher_id + 1) % philosophers_number

 
    forks[fork_left].acquire()
    forks[fork_right].acquire()
 

def eat(philosopher_id):
    print(f"Filósofo {philosopher_id} está comendo.")
    time.sleep(random.uniform(1, 3))

def drop_fork(philosopher_id):
    fork_left = philosopher_id
    fork_right = (philosopher_id + 1) % philosophers_number


    forks[fork_left].release()
    forks[fork_right].release()


if __name__ == "__main__":
    philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(philosophers_number)]

    for philosopher_thread in philosophers:
        philosopher_thread.start()

    for philosopher_thread in philosophers:
        philosopher_thread.join()