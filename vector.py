import random
import time
from tracemalloc import start

class vector():

    def __init__(self, vet):
        self.vet = vet

    def print(self):
        print("Vet:", self.vet)

    def fill(self):
        for i in range(0, 10000, 1):
            #if len(self.vet) == 0:
            self.vet.append(random.randint(0, 1000))
            '''n = random.randint(0,9999999999)
            for j in self.vet:
                if n not in self.vet:
                    self.vet.append(n)'''
    
    def order(self):
        for x in range(0, len(self.vet), 1):
            for j in range(x, len(self.vet), 1):
                if self.vet[x] > self.vet[j]:
                    n = self.vet[j]
                    self.vet[j] = self.vet[x]
                    self.vet[x] = n
            
    def insert(self):
        print("> INSERT <")
        print(self.vet)
        self.vet.append(None)
        size = len(self.vet)
        number = int(input("N:"))

        for i in range(0, len(self.vet), 1):
            if number < self.vet[i]:
                for x in range(size-1, i, -1):
                    n = self.vet[x]
                    self.vet[x] = self.vet[x-1]
                    self.vet[x-1] = n
                break
            else:
                self.vet[size-1] = number
                        
        for j in range(0, len(self.vet), 1):
            if self.vet[j] == None:
                self.vet[j] = number
                break
 
    def delete(self):
        print("> DELETE <")
        temporaryVet = []
        print(self.vet)
        n = int(input("N:"))

        for x in range(0, len(self.vet)-1, 1):
            if self.vet[x] == n:
                for i in range(x, len(self.vet)-1, 1):
                    n = self.vet[i]
                    self.vet[i] = self.vet[i+1]
                    self.vet[i+1] = n
                print(self.vet)
                break
        
        for x in range(0, len(self.vet)-1, 1):
            temporaryVet.append(0)
        
        for i in range(0, len(self.vet)-1, 1):
            temporaryVet[i] = self.vet[i]
        
        self.vet = temporaryVet


    def search_binary(self):
        print("> SEARCH BINARY <")
        item = int(input("N: "))
        c = 0
    
        left, right = 0, len(self.vet)-1
        ''' || Utilizando o try/except para quando o número não for encontrado o erro ser tratado. || '''
        startTime = time.time()
        try: 
            while left <= right:

                mid = (left + right) // 2

                if self.vet[mid] == item:

                    print("Index:",self.vet.index(item))

                    c = c+1

                    print("Loops:",c)
                    endTime = time.time()
                    print(startTime)
                    print(endTime)
                    return mid-1
                    

                elif self.vet[mid] > item:

                    right = mid - 1
                    c = c+1

                else:  # self.vet[mid] < item
                    left = mid + 1
                    c = c+1

            print("Item found!\nIndex: ", self.vet.index(item))
            print("Loops:",c)
            return -1
        
        except:
            print("The item is not on the vet!")
            print("Loops:",c)
            endTime = time.time()
            print("Start:", startTime)
            print("End:", endTime)

    
    def linear_search(self):
        n = int(input("N: "))
        index = 0
        startTime = time.time()
        for x in range(0, len(self.vet)-1, 1):
            if self.vet[x] == n:
                print("Value:", n, end ="|")
                print("Index:", index)
                endTime = time.time()
                print("Start:", startTime)
                print("End:", endTime)
                break
            index = index+1

obj = vector([])
obj.fill()
obj.order()
#obj.insert()
#obj.delete()
#obj.search_binary()
obj.print()
obj.linear_search()
