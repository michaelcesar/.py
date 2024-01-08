import random, time

class Lists():

    def __init__(self, list):
        self.list = list


    def text(self):
        self.list = ['L', 'I', 'S', 'T', 'S']
        
        for x in self.list:
            ''' O 'flush' trata o gargalo no buffer de memória. || '''
            print(x, end = '', flush= True)
            time.sleep(0.3)

        print('\n')

           
    def fill (self):

        size = int(input("Tamanho: "))
        ''' || Preencher lista com números em ordem crescente. || '''
        #for x in range (size):
            #self.list.append(x)


        ''' || Preencher lista com números aleatórios. || '''
        self.list = random.sample(range(size), size)


        ''' || Preencher com apenas uma linha de código. || '''
        #self.list = [x for x in range(10)]

        return self.list


    '''|| Exibindo itens de uma lista. || '''
    def display_start(self):

        #exibindo itens da lista do primeiro até o último
        for x in range(len(self.list)):
            print("_")
            print(self.list[x])
            ''' || Substitui o "\n" por algo que você deseja. || '''
            #print(x, end = ' ')

        return self.list

    '''|| Exibindo itens de uma lista v2. || '''
    def display_end(self):

        #exibindo itens da lista do último até o primeiro
        for x in range(len(self.list)-1, -1, -1):
            print(self.list[x])
            ''' || Substitui o "\n" por algo que você deseja. || '''
            #print(x, end = ' ')
            
    

    ''' || Inserindo um item numa lista. || '''
    def insert(self):
        Insert = int(input("Value: "))
        position = int(input("Position: "))
        print(self.list)
        self.list.insert(position, Insert)
        print(self.list, "\n")

        return self.list


    ''' || Excluindo o item de uma lista. || '''
    def delete(self):
        position = int(input("Position: "))
        '''' || Remover o item da lista com esse valor. || '''
        #self.list.remove(position)
        ''''|| Remover o indice da lista. || '''
        self.list.pop(position)

        return self.list

    def organize(self):
        ''' || A função 'sort' nativa do Python, organiza a lista em ordem crescente. || '''
        self.list.sort()
        print(self.list)

        return self.list
    

    ''' || Mostrar índice e valor contido no mesmo. || '''
    def indexes(self):
        [print (x,y) for x,y in enumerate(self.list)]

        return self.list

    ''' || Utilizando busca binária para encontrar o índice do item da lista desejado. || '''
    def search_binary(self):

        item = int(input("Number: "))
        
        left, right = 0, len(self.list) - 1
        ''' || Utilizando o try/except para quando o número não for encontrado o erro ser tratado. || '''
        try: 
            while left <= right:
                
                mid = (left + right) // 2

                if self.list[mid] == item:

                    print("Index:",self.list.index(item))
    
                    return mid-1
                    

                elif self.list[mid] > item:

                    right = mid - 1
                

                else:  # self.list[mid] < item
                    left = mid + 1
                    

            print("Item found!\nIndex: ", self.list.index(item))
            return -1
        
        except:
            print("The item is not on the list!")

        
    def max_value(self):
        max_value = max(self.list)
        print("The highest value in the list is: ", max_value)

        return self.list
    
    def min_value(self):
        min_value = min(self.list)
        print("The minimum value in the list is: ", min_value)

        return self.list



List = []
Lists(List).text()
#l = Lists(List).fill()
#l = Lists(l).insert()
#l = Lists(l).display_start()
#l = Lists(l).search_binary()
#l = Lists(l).max_value()
#l = Lists(l).min_value()
#l = Lists(l).organize()
#l = Lists(l).display_start()
#l = Lists(l).delete()
#l = Lists(l).display_start()
#l = Lists(l).indexes()