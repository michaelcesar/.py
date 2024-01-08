from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
     
print("-"*100)
print("x"*42, "BUSCA BINÁRIA", "x"*43)
print("-"*100)
tv = int(input("Escolha um tamanho para o vetor: \n>> "))
print("-"*100)
item = int(input("Escolha um número para ser buscado: \n>> "))
print("-"*100)

fig, ax = plt.subplots(figsize=(12, 6))
A = np.arange(0, tv, 1)
ax.set(xlim=(0, tv), ylim=(0, tv))
plt.xlabel('VETOR COM {} ELEMENTOS'.format(tv))


def pesquisa_binaria(A, item):
    contador = 0
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if A[meio] == item:
            ax.plot(meio, meio, "x", color= 'red')
            nome = str(contador) + '.png'
            plt.savefig(nome, dpi=200)
            contador = contador + 1
            print(contador)
            return meio-1
        elif A[meio] > item:
            ax.plot(meio, meio, "<")
            nome = str(contador) + '.png'
            plt.savefig(nome, dpi=200)
            contador = contador + 1
            print(contador)
            direita = meio - 1
        else:  # A[meio] < item
            ax.plot(meio, meio, ">")
            nome = str(contador) + '.png'
            plt.savefig(nome, dpi=200)
            contador = contador + 1
            print(contador)
            esquerda = meio + 1
    return -1

print("Número:", item)
print("Índice:", pesquisa_binaria(A, item))

# Create the frames
frames = []
imgs = glob.glob("*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

# Salvar em um arquivo GIF que faz um loop para sempre
frames[0].save('busca_binaria.gif', format='GIF',
               append_images=frames[0:],
               save_all=True,
               duration=600, loop=0)


