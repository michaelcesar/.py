class Fibonacci():

    def sequence (a = 1, b = 0, c = 0, max = 0):

        max = int(input("Max: "))

        for x in range(max):

            print(a)

            c = a
            a = a+b
            b = c


object = Fibonacci.sequence()
