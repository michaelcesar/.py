import os

class Contact:
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email
       
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
    

    def saveContact(self, name, phone, email):
        if len(agenda) < 5:
            agenda.append((name, phone, email))
        else:
            print('Agenda lotada!')
            print(f'Contato salvo!')

    def removeContact(self, name):
        for i in agenda:
            if i[0] == name:
                agenda.remove(i)
                print(f'Contato removido')

    def searchContact(self, name):
        c = 0
        for i in agenda:
            c = c+1
            if i[0] == name:
                print("-"*20)
                print("Indíce: ", c-1)
                print("Nome do contato: ", i[0])
                
    def printBook(self):
        c = 0
        for i in agenda:
            c = c+1
            print("-"*20)
            print("Contato", c-1)
            for x in i:
                print(x)

    def printContact(self, index):
            print("-"*20)
            print("Contato detalhado: ")
            for x in agenda[index]:
                print(x)

agenda = []
c = 0
option = 0
while c == 0:
    print("\n\n\nAdicionar contato (1)\nRemover contato (2)\nProcurar contato(3)\nExibir contato(4)\nExibir todos os contatos da agenda(5)\nEncerrar agenda(6)\n")
    option = int(input(">> "))
    if option == 1:
        contact = Contact(input("Nome:"), input("Número: "), input("Email: "))
        contact.saveContact(contact.name, contact.phone, contact.email)
    elif option == 2:
        contact.removeContact(input("Nome:"))
    elif option == 3:
        contact.searchContact(input("Nome:"))
    elif option == 4:
        contact.printContact('Índice: ')
    elif option == 5:
        contact.printBook()
    elif option == 6:
        c = 1
    else:
        print("Escolha uma opção válida!")
