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
    

    def expression(self):
        expression = input("Digite sua expressão matemática: ")

        for i in expression:

            if i == '{':
                pile.append('}')
            
            if i == '[':
                pile.append(']')
            
            if i == '(':
                pile.append(')')
        
        print("Main: ")
        pile.print()

        for i in expression:
            
            if i == ')':
                if self.top.value == i:
                    pile.remove()

            if i == ']':
                if self.top.value == i:
                    pile.remove()

            if i == '}':
                if self.top.value == i:
                    pile.remove()
            


        print("Over")
        pile.print()
        
        if self.top:
            print("Expressão errada!")
        else:
            print("Expressão correta!")
            
        
        





pile = Pile()
pile.expression()
        
        
        


