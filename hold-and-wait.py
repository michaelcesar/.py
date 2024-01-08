import threading
import time
import random

number_philosopher = 5
forks = [threading.Semaphore(1) for _ in range(number_philosopher)]
blocked = [False] * number_philosopher

def philosopher(philosopher_id):
    while True:
        think(philosopher_id)
        get_forks(philosopher_id)
        eat(philosopher_id)
        drop_forks(philosopher_id)

def think(philosopher_id):
    print(f"Filósofo {philosopher_id} está pensando.")
    time.sleep(random.uniform(1, 1))

def get_forks(philosopher_id):
    fork_left = philosopher_id
    fork_right = (philosopher_id + 1) % number_philosopher

    while True:
        if not forks[fork_left].acquire(blocking=False):
            print(f"Filósofo {philosopher_id} soltou o garfo esquerdo e pensou, pois não está disponível.")
            think(philosopher_id)
        elif not forks[fork_right].acquire(blocking=False):
            forks[fork_left].release()
            print(f"Filósofo {philosopher_id} soltou o garfo direito e pensou, pois não está disponível.")
            think(philosopher_id)
        else:
            break

def eat(philosopher_id):
    print(f"Filósofo {philosopher_id} está comendo.")
    time.sleep(random.uniform(1, 1))

def drop_forks(philosopher_id):
    fork_left = philosopher_id
    fork_right = (philosopher_id + 1) % number_philosopher

    forks[fork_left].release()
    forks[fork_right].release()

if __name__ == "__main__":
    philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(number_philosopher)]

    for philosopher_thread in philosophers:
        philosopher_thread.start()

    for philosopher_thread in philosophers:
        philosopher_thread.join()