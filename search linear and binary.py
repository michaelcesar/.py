import time, psutil


def listGenerator(n):
    list = []
    for i in range(n):
        list.append(i)
    return list

def linear_search(list, number):
    for i, element in enumerate(list):
        if element == number:
            print(f"{number} foi encontrado")
            return i 
    return -1

def binary_search(list, number):
    left, right = 0, len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        if list[mid] == number:
            print(f"{number} foi encontrado")
            return mid  
        elif list[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1  

process = psutil.Process()
elements = 100000000
list = listGenerator(elements)
#print(list)

#------------------------
""" start_cpu = process.cpu_percent()
start_memory = process.memory_info().rss
start_time = time.time()
linear = linear_search(list, 9999999)
end_time = time.time()
linear_time = start_time - end_time
end_cpu = process.cpu_percent()
end_memory = process.memory_info().rss
print(f"Tempo de execução da busca linear: {linear_time:.6f} segundos")
print(f"Uso de CPU durante a busca linear: {end_cpu - start_cpu:.2f}%")
print(f"Uso de memória durante a busca linear: {end_memory - start_memory} bytes") """
#------------------------

#------------------------
start_cpu = process.cpu_percent()
start_memory = process.memory_info().rss
start_time = time.time()
binary = binary_search(list, 50000000)
end_time = time.time()
binary_time = start_time - end_time
end_cpu = process.cpu_percent()
end_memory = process.memory_info().rss
print(f"Tempo de execução da busca binária: {binary_time:.6f} segundos")
print(f"Uso de CPU durante a busca binária: {end_cpu - start_cpu:.2f}%")
print(f"Uso de memória durante a busca binária: {end_memory - start_memory} bytes")
#------------------------
