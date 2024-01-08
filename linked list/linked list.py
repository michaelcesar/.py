from operator import index
from re import I
from numpy import size
from node import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0
        #tamanho da lista.
    
    def print(self):
        #um ponteiro que aponta para a cabeça da lista.
        print("[ ", end="")
        pointer = self.head
        #enquanto o 'pointer' for diferente de 'None'.
        while (pointer.next):
            print(pointer.data, "-> ", end="")
            #aqui passamos o próximo nó para o ponteiro.
            pointer = pointer.next
        else:
            #printar o 'dado' do último nó da lista.
            print(pointer.data, "]")
    
    #adicionando um novo elemento ao final da lista
    def append(self, element):
        #inserção quando a lista já possui elementos('nós').
        if self.head:
            #um ponteiro que aponta para a cabeça da lista.
            pointer = self.head
            #enquanto o 'pointer' for diferente de 'None'.
            while(pointer.next):
                pointer = pointer.next
                #aqui passamos o próximo nó para o ponteiro.
            pointer.next = Node(element)
            #quando o 'next' do nó for 'None', então no 'next'
            #desse nó recebe o novo nó.
        else:
            #primeira inserção
            self.head = Node(element)
        self._size = self._size+1
    
    #sobrecarga de operador
    def __len__(self):
        return self._size
        #retornar o valor que está em 'self.size' ao usar a
        #função 'len' do python.

    #sobrecarga de operador
    #acessando nós da lista encadeada por seu indices.
    def __getitem__(self, index):
        #sintaxe do metodo
        # list[8]
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")

        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    #sobrecarga de operador
    #substituindo nós da lista encadeada por seu indices.
    def __setitem__(self, index, element):
        #sintaxe do metodo
        #list [8] = 9
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")

        if pointer:
            pointer.data = element
        else:
            raise IndexError("list index out of range")
    
    #metodo para deletar um elemento da lista encadeada
    def delete(self, element):
        pointer = self.head
        for i in range(self._size):
            if element == pointer.data:
                previous.next = pointer.next
                pointer = previous
                break
            previous = pointer
            pointer = pointer.next
    

    def count(self, element):
        pointer = self.head
        count = 0
        for i in range(self._size):
            if element == pointer.data:
                count = count+1
            pointer = pointer.next

        print(count)
    
    #função para saber o indice de um elemento na lista
    #uma busca linear
    def index(self, element):
        #um ponteiro que aponta para a cabeça da lista.
        pointer = self.head
        #contador para definir o indice
        i = 0
        #enquanto existir um ponteiro
        while(pointer):
            #se o 'dado' desse ponteiro for igual ao elemento que estamos querendo saber o indice
            if pointer.data == element:
                #retorne o valor da variavel 'i'
                return i 
            #se não, o ponteiro agora recebe o próximo nó e a verificação será feita nele
            pointer = pointer.next
            #e também é somado '+1' ao contador, contabilizando o indice correto
            i = i+1
        
        raise ValueError("{} is not in list".format(element))


    def reverse(self):
        #um ponteiro que aponta para a cabeça da lista e o valor atual do envelope
        current = self.head
        #um ponteiro para receber o valor anterior do envelope
        previous = None
        #um ponteiro para receber o próximo valor do envelope
        next = None
        #enquanto o 'envelope' for diferente de 'None', ou seja, enquanto existir um 
        #evelope que aponte para um próximo envelope.

        #esse metodo inverte toda a lista
        while (current != None):
            next = current.next
            current.next = previous
            previous = current
            current = next

        #mudando a cabeça da lista para a mesma poder percorrer na ordem inversa.
        self.head = previous
        
        #chamando o metodo de print
        list.print()
    
    #função para verificar se duas listas encadeadas são iguais
    def verify(self):
        #variavel para controlar os prints da função
        trash = 0
        #ponteiro
        pointer = self.head
        #ponteiro
        pointer2 = list2.head
        #enquanto o 'pointer' for diferente de 'None'.
        while (pointer.next):
            while(pointer2.next):
                if pointer.data == pointer2.data:
                    pointer = pointer.next
                    pointer2 = pointer2.next
                else:
                    trash += 1
                    pointer = pointer.next
                    pointer2 = pointer2.next
                    print("As listas são diferentes!")
                    break
        else: 

            if pointer.data == pointer2.data:
                pass
            else:
                trash += 1
                pointer = pointer.next
                pointer2 = pointer2.next
                print("As listas são diferentes!")

        if trash == 0:   
            print("As listas são iguais!")


    '''
    def verify(self):
        List = []
        List2 = []

        pointer = self.head
        pointer2 = list2.head
        #enquanto o 'pointer' for diferente de 'None'.
        while (pointer.next):
            List.append(pointer.data)
            #aqui passamos o próximo nó para o ponteiro.
            pointer = pointer.next
        else:
            List.append(pointer.data)
            print(List)
        
        while (pointer2.next):
            List2.append(pointer2.data)
            #aqui passamos o próximo nó para o ponteiro.
            pointer2 = pointer2.next
        else:
            List2.append(pointer2.data)
            print(List2)

        for List, List2 in zip (List, List2):
            trash = 0
            if List == List2:
                pass
            else:
                print("As listas são diferentes!")
                trash += 1
                break
                
        if trash == 0:
            print("As listas são iguais!")
    '''      


#> = Comandos -  Apague a hashtag para rodar o comando.

list = LinkedList()
list2 = LinkedList()
#criando a lista vazia
#>print(list.size)
#vendo tamanho da lista
#------------------------------------
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
#------------------------------------
list2.append(1)
list2.append(2)
list2.append(3)
list2.append(4)
list2.append(5)
#------------------------------------
#>print(len(list))
#>print(list[0])
#>print(list[1])
list.print()
list2.print()
#>list2.print()
#>list[2] = 1
list.delete(5)
list.print()
#>list.print()
#>print(list.index(10))
#>list.count(3)
#>list.reverse()
#>list2.reverse()
#>list.verify()
