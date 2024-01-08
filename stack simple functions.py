import os

class Object:

    def __init__(self, value):
        self.value = value
        self.previous = None



class Pile:

    def __init__(self):
        self.top = None

    

    def append(self, value):

        if self.top:
            pointer = self.top
            self.top = Object(value)
            self.top.previous = pointer
        
        else:
            self.top = Object(value)

    
    def remove(self):

        if self.top:
            self.top = self.top.previous
        else:
            print("Pilha vazia!")
    

    def print(self):

        if self.top:
            pointer = self.top

            while pointer.previous:
                print(pointer.value)
                pointer = pointer.previous

            print(pointer.value)

        else:
            print("Pilha vazia!")
    
    def reverse(self):
        pile2 = Pile()

        while self.top:
            pile2.append(self.top.value)
            pile.remove()

        pile2.print()  

pile = Pile()

while True:
    print("Add (1) | Item remove (2) | Reverse (3)")
    option = int(input("Select: "))

    if option == 1:
        os.system('cls')
        pile.print()
        pile.append(input("Value: "))
        os.system('cls')
        pile.print()

    if option == 2:
        os.system('cls')
        pile.remove()
        pile.print()
        
    if option == 3:
        pile.reverse()
    
