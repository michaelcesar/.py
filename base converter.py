""" Algumas funções podem não estar funcionando corretamente, caso queira corrigir, ficarei grato!"""

import time, math

class Converter():

    def __init__(self, number, list):
        self.number = number 
        self.list= list
    

    def decimal_to_binary(self):

        print(" -"*50,"\n Convert a decimal number to binary.\n","- "*50)
        self.number = int(input(" Number: "))

        while self.number > 1:

            if self.number%2 < 1:

                self.list.append(0)
                self.number = self.number/2

            else:
                self.list.append(1)
                self.number = self.number/2
            

        for x in range(len(self.list)-1, -1, -1):
            print(self.list[x], end='|', flush = True)
            time.sleep(0.3)
    

    def binary_to_decimal(self):

        print(" -"*50,"\n Convert a binary number to decimal.\n","- "*50)
        self.number = input("Number: ")
        self.number = list(self.number)

        b = 0
        n = 0

        for x in range(len(self.number)-1, -1, -1):

            self.number[x] = int(self.number[x])
            n = 2**b
            n = self.number[x]*n
            b = b+1
            self.list.append(int(n))

        for x in range(0, len(self.list), 1):
            print(self.list[x], end='|', flush = True)
            time.sleep(0.3)
        
        print ("\n","\nYou number in decimal: ",sum(self.list))



    def decimal_for_octal(self):

        print(" -"*50,"\n Convert a decimal number to octal.\n","- "*50)
        self.number = int(input("Number: "))

        while self.number > 1:

            n = self.number%8
            self.list.append(int(n))
            self.number = self.number/8
            

        
        print("\nYou number in decimal: ")
        for x in range(len(self.list)-1, -1, -1):
            print(self.list[x], end='')
            


    def octal_for_decimal(self):

        print(" -"*50,"\n Convert a octal number to decimal.\n","- "*50)
        self.number = input("Number: ")
        self.number = list(self.number)

        b = 0
        n = 0

        for x in range(len(self.number)-1, -1, -1):

            self.number[x] = int(self.number[x])
            n = 8**b
            n = self.number[x]*n
            b = b+1
            self.list.append(int(n))    

            for x in range(0, len(self.list), 1):
                print(self.list[x], end='|', flush = True)
                time.sleep(0.3)
        
        print ("\n","\nYou number in decimal: ",sum(self.list)) 
    


    def decimal_for_hexadecimal(self):
        print(" -"*50,"\n Convert a decimal number to hexadecimal.\n","- "*50)
        self.number = str(input("Number: "))
        self.number = list(self.number)
        b = 0

        for x in range(len(self.number)-1, -1, -1):

            if self.number[x] == 'A' or self.number[x] == 'a':
                self.number[x] = int(10)
                self.number[x] = (16**b)*self.number[x]
                b = b+1
            
            elif self.number[x] == 'B' or self.number[x] == 'b':
                self.number[x] = int(11)
                self.number[x] = (16**b)*self.number[x]
                b = b+1
            
            elif self.number[x] == 'C' or self.number[x] == 'c':
                self.number[x] = int(12)
                self.number[x] = (16**b)*self.number[x]
                b = b+1
            
            elif self.number[x] == 'D' or self.number[x] == 'd':
                self.number[x] = int(13)
                self.number[x] = (16**b)*self.number[x]
                b = b+1
            
            elif self.number[x] == 'E' or self.number[x] == 'e':
                self.number[x] = int(14)
                self.number[x] = (16**b)*self.number[x]
                b = b+1
            
            elif self.number[x] == 'F' or self.number[x] == 'f':
                self.number[x] = int(15)
                self.number[x] = (16**b)*self.number[x]
                b = b+1

            else:
                self.number[x] = int(self.number[x])
                self.number[x] = (16**b)*self.number[x]
                b = b+1
        

        for x in range(0, len(self.number), 1):
                print(self.number[x], end='|', flush = True)
                time.sleep(0.3)

        print ("\n","\nYou number in decimal: ",sum(self.number)) 

    

    def hexadecimal_for_decimal(self):

        print(" -"*50,"\n Convert a hexadecimal number to decimal.\n","- "*50)
        self.number = str(input("Number: "))
        self.number = list(self.number)
        b = 0

        for x in range(len(self.number)-1, -1, -1):

            if self.number[x] == 'A' or self.number[x] == 'a':
                self.number[x] = int(10)
                self.number[x] = (16**b)*self.number[x]
                b = b+1
            
            elif self.number[x] == 'B' or self.number[x] == 'b':
                self.number[x] = int(11)
                self.number[x] = (16**b)*self.number[x]
                b = b+1
            
            elif self.number[x] == 'C' or self.number[x] == 'c':
                self.number[x] = int(12)
                self.number[x] = (16**b)*self.number[x]
                b = b+1
            
            elif self.number[x] == 'D' or self.number[x] == 'd':
                self.number[x] = int(13)
                self.number[x] = (16**b)*self.number[x]
                b = b+1
            
            elif self.number[x] == 'E' or self.number[x] == 'e':
                self.number[x] = int(14)
                self.number[x] = (16**b)*self.number[x]
                b = b+1
            
            elif self.number[x] == 'F' or self.number[x] == 'f':
                self.number[x] = int(15)
                self.number[x] = (16**b)*self.number[x]
                b = b+1

            else:
                self.number[x] = int(self.number[x])
                self.number[x] = (16**b)*self.number[x]
                b = b+1
        

        for x in range(0, len(self.number), 1):
                print(self.number[x], end='|', flush = True)
                time.sleep(0.3)

        print ("\n","\nYou number in decimal: ",sum(self.number)) 




obj = Converter(0 ,[]).decimal_for_hexadecimal()

