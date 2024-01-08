class Elevador():

    def __init__(self, floors = 0, capacity = 0, number = 0, current = 0):
        self.__floors = floors
        self.__capacity = capacity
        self.__number = number
        self.__current = current

        self.__floors = int(input("Número de andares: "))
        self.__capacity = int(input("Capacidade do elevador:"))

    def floorsGet(self):
        return self.__floors

    def floorsSet(self, floors):
        self.__floors = floors
    
    
    def capacityGet(self):
        return self.__capacity

    def capacitySet(self, capacity):
        self.__capacity = capacity
    

    def numberGet(self):
        return self.__number

    def numberSet(self, number):
        self.__number = number
    
    
    def currentGet(self):
        return self.__current

    def currentSet(self, current):
        self.__current = current


    def Entrar(self):

        if self.__number < self.__capacity:
            self.__number = self.__number +1
            print("Uma pessoa está entrando no elevador...")
            print("Número de pessoas no elevador: ", self.__number)
            print("O elevador está no andar: ", self.__current)
            print("-"*30)
            
        else:
            print("O elevador atingiu sua capacidade máxima!")
            print("O elevador está no andar: ", self.__current)
            print("-"*30)

    def Sair(self):

        if self.__number > 0:
            self.__number = self.__number -1
            print("Uma pessoa está saindo do elevador...")
            print("Número de pessoas no elevador: ", self.__number)
            print("O elevador está no andar: ", self.__current)
            print("-"*30)
        else:
            print("O elevador está vázio!")
            print("O elevador está no andar: ", self.__current)
            print("-"*30)

    def Subir(self):
      
        if self.__current < self.__floors:
            self.__current = self.__current +1
            print("O elevador está subindo um andar...")
            print("O elevador está no andar: ", self.__current)
            print("Número de pessoas no elevador: ", self.__number)
            print("-"*30)
        else:
            print("O elevador está no último andar!")
            print("Número de pessoas no elevador: ", self.__number)
            print("-"*30)


    def Descer(self):

        if self.__current > 0:
            self.__current = self.__current - 1
            print("O elevador está descendo um andar...")
            print("O elevador está no andar: ", self.__current)
            print("Número de pessoas no elevador: ", self.__number)
            print("-"*30)
        else:
            print("O elevador está no térreo!")
            print("Número de pessoas no elevador: ", self.__number)
            print("-"*30)


elevador = Elevador()

c = 0

while c == 0:
    choice = int(input("ELEVADOR\nEntrar(1)\nSair(2)\nSubir(3)\nDescer(4)\nEncerrar(5)\n\n>>:"))
    
    if choice == 1:
        elevador.Entrar()
    elif choice ==2:
        elevador.Sair()
    elif choice ==3:
        elevador.Subir()
    elif choice ==4:
        elevador.Descer()
    elif choice ==5:
        print("Elevador encerrado!")
        c = 1
    else:
        print("Escolha uma opção válida!")


