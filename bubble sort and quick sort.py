import random, time, psutil

def numbersGenerator(n, min, max):
    list = []
    for x in range(n):
        number = random.randint(min, max)
        list.append(number)
    return list


def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                #troca dos elementos
                list[j], list[j + 1] = list[j + 1], list[j]


def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivot = lista[len(lista) // 2] 
    smallers, equals, biggers = [], [], []
    
    for element in lista:
        if element < pivot:
            smallers.append(element)
        elif element == pivot:
            equals.append(element)
        else:
            biggers.append(element)
    
    return quick_sort(smallers) + equals + quick_sort(biggers)


process = psutil.Process()
elements = 10000
min = 1
max = 10000
list = numbersGenerator(elements, min, max)
#print(list)



#-------------------------
start_cpu = process.cpu_percent()
start_memory = process.memory_info().rss
start_time = time.time()
bubble_sort(list)
end_time = time.time()
bubble_sort_time = start_time - end_time
end_cpu = process.cpu_percent()
end_memory = process.memory_info().rss
print(f"Tempo de execução do bubble sort: {bubble_sort_time:.6f} segundos")
print(f"Uso de CPU durante o bubble sort: {end_cpu - start_cpu:.2f}%")
print(f"Uso de memória durante o bubble sort: {end_memory - start_memory} bytes")
#-------------------------

print("----------")

#-------------------------
start_cpu = process.cpu_percent()
start_memory = process.memory_info().rss
start_time = time.time()
list = quick_sort(list)
end_time = time.time()
quick_sort_time = start_time - end_time
end_cpu = process.cpu_percent()
end_memory = process.memory_info().rss
print(f"Tempo de execução do quick sort: {quick_sort_time:.6f} segundos")
print(f"Uso de CPU durante o quick Sort: {end_cpu - start_cpu:.2f}%")
print(f"Uso de memória durante o quick sort: {end_memory - start_memory} bytes")
#-------------------------
