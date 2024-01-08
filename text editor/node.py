class Node:
    #data - guarda o dado do nó.
    #next - guarda a posição do próximo nó.
    #essa estrutura é apenas um envelope, algo para
    #envelopar(guardar) o dado e a posição do próximo nó.
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

node1 = Node(8)
#Criei um nó chamado 'node1' e estou inserindo
#o valor 8 dentro da posição do nó que guarda
#o valor, a posição 'data'.
node2 = Node(10)
#Criei um nó chamado 'node2' e estou inserindo
#o valor 10 dentro da posição do nó que guarda
#o valor, a posição 'data'.
node3 = Node(2)
#Criei um nó chamado 'node3' e estou inserindo
#o valor 2 dentro da posição do nó que guarda
#o valor, a posição 'data'.

#>print(node1.data)
#Instanciando o valor que está dentro do 'data'
#do 'node1'
#>print(node2.data)
#Instanciando o valor que está dentro do 'data'
#do 'node2'
node2.previous = node1
node2.next = node3
#Agora estou colocando o 'node2' dentro do espaço
#reservado para guardar a posição do próximo nó do 'node1'
#assim, o 'node1' terá seu valor e também uma referência para o
#próximo nó, o 'node2'.
#>print(node1.next.data)
'''node1 = nó
   next = próximo nó
   data = valor que está no próximo nó.
'''
#aqui instanciando o 'node1', podemos ver também o valor que está dentro
#do próximo nó, o 'node2'.


