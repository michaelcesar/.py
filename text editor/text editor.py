""" Este código é um editor simples de texto que faz o uso de forma trivial de uma lista encadeada para criar os textos. """

from node import Node
import os
import keyboard
import time

class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0
        #tamanho da lista.
    
    def print(self):
        #um ponteiro que aponta para a cabeça da lista.
        pointer = self.head
        #enquanto o 'pointer' for diferente de 'None'.
        while (pointer.next):
            print(pointer.data, end="")
            '''print(pointer.previous,"]", "[",pointer.data,"]", "[", pointer.next, "]", "-> ", end="")'''
            #aqui passamos o próximo nó para o ponteiro.
            pointer = pointer.next
        else:
            #printar o 'dado' do último nó da lista.
            print(pointer.data, end="")
    
    def save(self):
        archive = open(input("Archive: ")+'.txt','w')
        #um ponteiro que aponta para a cabeça da lista.
        pointer = self.head
        #enquanto o 'pointer' for diferente de 'None'.
        while (pointer.next):
            archive.write(pointer.data)
            '''print(pointer.previous,"]", "[",pointer.data,"]", "[", pointer.next, "]", "-> ", end="")'''
            #aqui passamos o próximo nó para o ponteiro.
            pointer = pointer.next
        else:
            #printar o 'dado' do último nó da lista.
            archive.write(pointer.data)

    def printDetails(self):
        #um ponteiro que aponta para a cabeça da lista.
        pointer = self.head
        #enquanto o 'pointer' for diferente de 'None'.
        while (pointer.next):
            print("[", end="")
            print(pointer.previous, "|", pointer.data,"|", pointer.next, end="]")
            '''print(pointer.previous,"]", "[",pointer.data,"]", "[", pointer.next, "]", "-> ", end="")'''
            #aqui passamos o próximo nó para o ponteiro.
            pointer = pointer.next
        else:
            #printar o 'dado' do último nó da lista.
            print("[", end="")
            print(pointer.previous, "|", pointer.data,"|", pointer.next, end="]")

    def printNode(self):
        #um ponteiro que aponta para a cabeça da lista.
        pointer = self.head
        #enquanto o 'pointer' for diferente de 'None'.
        while (pointer.next):
            print("[", end="")
            print(pointer.data, end="]")
            '''print(pointer.previous,"]", "[",pointer.data,"]", "[", pointer.next, "]", "-> ", end="")'''
            #aqui passamos o próximo nó para o ponteiro.
            pointer = pointer.next
        else:
            #printar o 'dado' do último nó da lista.
            print("[", end="")
            print(pointer.data, end="]")

    #adicionando um novo elemento ao final da lista
    def append(self, element):
        previous = None
        #inserção quando a lista já possui elementos('nós').
        if self.head:
            #um ponteiro que aponta para a cabeça da lista.
            pointer = self.head
            #enquanto o 'pointer' for diferente de 'None'.
            while(pointer.next):
                pointer = pointer.next
            #aqui passamos o próximo nó para o ponteiro.
            previous = pointer
            #armazenando o ponteiro atual em uma variavel
            
            pointer.next = Node(element)
            pointer.next.previous = previous
            #quando o 'next' do nó for 'None', então no 'next'
            #desse nó recebe o novo nó.
            #e o seu 'previous' recebe o nó antigo armazenado
            #na variável previous
        else:
            #primeira inserção
            self.head = Node(element)
            previous = self.head
        self._size = self._size+1
    

    def appendMid(self, index, element):
        atual = None
        max = 0
        #inserção quando a lista já possui elementos('nós').
        if self.head:
            #um ponteiro que aponta para a cabeça da lista.
            pointer = self.head
            #enquanto o 'pointer' for diferente de 'None'.
            while(pointer.next):
                max += 1
                if max == index:
                    atual = Node(element)
                    atual.next = pointer.next
                    atual.previous = pointer
                    pointer.next = atual
                    self._size = self._size+1
                    break

                pointer = pointer.next
          
    
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


caracteres = ['a','b','c', 'ç','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '1', 
         '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '!', '+', '-', '(', ')', '[', ']', '{', '}', '.']


list = LinkedList()
""" list.append('')
pointer = 0
max = 1
pointer = 1 """

#-------

list.append('')
max = 1
pointer = 1

archive = open(input("Archive: ")+".txt",'r')
text = ''

for archive in archive:
    text = archive

for text in text:
    list.append(text)
    pointer +=1
    max +=1

#------- 

while True:

    char = keyboard.get_hotkey_name()

    if len(char)> 0:
        """ print(char) """
        char = str(char)
                  
        for a in caracteres:
            if keyboard.is_pressed(char):
                if char == a:
                    if pointer == max:
                        list.append(char)
                        pointer += 1
                        max += 1
                        os.system('cls')
                        list.print()
                        print("\n")
                        list.printNode()
                        """ print("\n")
                        list.printDetails() """
                        print("\n")
                        time.sleep(0.08)
                        char = 0
                        print(list[pointer-1], ">")
                        continue
                    else:
                        list.appendMid(pointer, char)
                        pointer += 1
                        max += 1
                        os.system('cls')
                        list.print()
                        print("\n")
                        list.printNode()
                        print("\n")
                        time.sleep(0.08)
                        char = 0
                        print(list[pointer-1], ">")
                        continue

            
                if char == 'space':
                    if pointer == max:
                        list.append(' ')
                        pointer += 1
                        max += 1
                        os.system('cls')
                        list.print()
                        print("\n")
                        list.printNode()
                        """ print("\n")
                        list.printDetails() """
                        print("\n")
                        time.sleep(0.08)
                        char = 0
                        print(list[pointer-1], ">")
                        continue
                    else:
                        list.appendMid(pointer, ' ')
                        pointer += 1
                        max += 1
                        os.system('cls')
                        list.print()
                        print("\n")
                        list.printNode()
                        print("\n")
                        time.sleep(0.08)
                        char = 0
                        print(list[pointer-1], ">")
                        continue

                if char == 'backspace':
                    if pointer > 1:
                        if pointer == max:
                            list[pointer-1] = None
                            list.delete(None)
                            os.system('cls')
                            list.print()
                            print("\n")
                            list.printNode()
                            print("\n")
                            time.sleep(0.08)
                            char = 0
                            pointer -= 1
                            max -=1
                            print(list[pointer-1], ">")
                            continue
                        else:
                            list[pointer-1] = None
                            list.delete(None)
                            os.system('cls')
                            list.print()
                            print("\n")
                            list.printNode()
                            print("\n")
                            time.sleep(0.08)
                            char = 0
                            pointer -= 1
                            max -=1
                            print(list[pointer-1], ">")
                            continue

                if char == 'left':
                    if pointer > 0:
                        pointer -= 1
                        os.system('cls')
                        list.print()
                        print("\n")
                        list.printNode()
                        print("\n")
                        time.sleep(0.08)
                        char = 0
                        print(list[pointer-1], ">")
                        continue

                if char == 'right':
                    if pointer < max:
                        pointer += 1
                        os.system('cls')
                        list.print()
                        print("\n")
                        list.printNode()
                        print("\n")
                        time.sleep(0.08)
                        char = 0
                        print(list[pointer-1], ">")
                        continue
                
                if char == '´':
                    while True:
                        switch = keyboard.get_hotkey_name()
                        if switch == 'e':
                            if pointer == max:
                                list.append('é')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                            else:
                                list.appendMid(pointer, 'é')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                        elif switch == 'a':
                            if pointer == max:
                                list.append('á')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                            else:
                                list.appendMid(pointer, 'á')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break
                        
                        elif switch == 'o':
                            if pointer == max:
                                list.append('ó')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                            else:
                                list.appendMid(pointer, 'ó')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break
                        
                        elif switch == 'i':
                            if pointer == max:
                                list.append('í')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                            else:
                                list.appendMid(pointer, 'í')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break
                        
                        elif switch == 'u':
                            if pointer == max:
                                list.append('ú')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                            else:
                                list.appendMid(pointer, 'ú')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break
               
                if char == '~':
                    while True:
                        switch = keyboard.get_hotkey_name()

                        if switch == 'a':
                            if pointer == max:
                                list.append('ã')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                            else:
                                list.appendMid(pointer, 'ã')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break
                        
                        elif switch == 'o':
                            if pointer == max:
                                list.append('õ')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                            else:
                                list.appendMid(pointer, 'õ')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                if char == 'enter':
                    if pointer == max:
                        list.append('\n')
                        pointer += 1
                        max += 1
                        os.system('cls')
                        list.print()
                        print("\n")
                        list.printNode()
                        print("\n")
                        time.sleep(0.08)
                        char = 0
                        print(list[pointer-1], ">")
                        continue
                    else:
                        list.appendMid(pointer, '\n')
                        pointer += 1
                        max += 1
                        os.system('cls')
                        list.print()
                        print("\n")
                        list.printNode()
                        print("\n")
                        time.sleep(0.08)
                        char = 0
                        print(list[pointer-1], ">")
                        continue

                if char == '^':
                    while True:
                        switch = keyboard.get_hotkey_name()
                        if switch == 'e':
                            if pointer == max:
                                list.append('ê')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                            else:
                                list.appendMid(pointer, 'ê')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                        elif switch == 'a':
                            if pointer == max:
                                list.append('â')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                            else:
                                list.appendMid(pointer, 'â')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break
                        
                        elif switch == 'o':
                            if pointer == max:
                                list.append('ô')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                            else:
                                list.appendMid(pointer, 'ô')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break
                        
                        elif switch == 'i':
                            if pointer == max:
                                list.append('î')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                            else:
                                list.appendMid(pointer, 'î')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break
                        
                        elif switch == 'u':
                            if pointer == max:
                                list.append('û')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break

                            else:
                                list.appendMid(pointer, 'û')
                                pointer += 1
                                max += 1
                                os.system('cls')
                                list.print()
                                print("\n")
                                list.printNode()
                                print("\n")
                                time.sleep(0.08)
                                char = 0
                                print(list[pointer-1], ">")
                                break
                                
                if char == '-':
                    list.save()
                    break                    
    continue
