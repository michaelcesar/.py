import time

class Object:
    def __init__(self, number, sequence):
        self.number = number
        self.sequence = sequence

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def insert(self, number, sequence):
        self.table[number] = Object(number, sequence)

    def search(self, number):
        if number < self.size and self.table[number] is not None:
            return self.table[number]
        return None

class Collatz:
    def __init__(self, cache):
        self.cache = cache

    def collatz(self, number):
        length = 1
        original_number = number

        while number != 1:
            cached_obj = self.cache.search(number)
            if cached_obj is not None:
                length += cached_obj.sequence - 1
                break

            if number % 2 == 0:
                number = number // 2
            else:
                number = 3 * number + 1
            length += 1

        self.cache.insert(original_number, length)
        return length

def find_collatz(limit):
    table = HashTable(limit)
    max_size = 1
    max_number = 1

    collatz_calculator = Collatz(table)

    for number in range(1, limit):
        if table.table[number] is None:
            size = collatz_calculator.collatz(number)
            if size > max_size:
                max_size = size
                max_number = number

    return max_number, max_size

limit = 1000000

start_time = time.time()
max_number, max_size = find_collatz(limit)
end_time = time.time()

time = end_time - start_time

print(f"O número {max_number} produz a sequência mais longa com {max_size} itens.")
print(f"Tempo de execução: {time} segundos")