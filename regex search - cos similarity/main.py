import re
import unicodedata
from sklearn.metrics.pairwise import cosine_similarity



class Txt:
    def __init__(self, list):
        self.list = list


    def txt(self):
        """   |Nome do Arquivo.| |Modo usado.||Formato do texto.|   """
        with open('corpus.txt', mode ='r', encoding = 'utf-8') as c:
            self.list = c.read()

        #return list
        return self.list[:1000]

    def remove(self):
        self.list = self.txt() 
        """"   |Remover os acentos.|   """
        newlist = unicodedata.normalize(u'NFKD', self.list).encode('ascii', 'ignore').decode('utf8')
        """"   |Remover caracteres especiais usando Regex.|   """
        endlist = (re.sub('[^a-zA-z_]+',' ', newlist))
        """"   |Retornar lista sem caracters especiais.|   """
        return(endlist)
        
    
class Search(Txt):
    def __init__(self, list):
        Txt.__init__(self, list)
    """"   |PESQUISA|    """
    def ctrlF(self):
        sm = float(0.80)
        cont = int(0)
        cs = float(0)
        listx = []
        listy = []
        listcharx = []
        """"   |Usando a função remove para acessar e tratar a lista.|   """
        endlist = self.remove()
        #print(endlist)
        """"    |Obter palavra a ser buscada.|            """
        word = str(input(">> "))
        """"     |Lista Cos0 X|      """
        for x in range (0, len(word), 1):
            """"   |Adicionando o valor 1 aos índices da lista vazia.|   """
            listx.append(1)
            """" |Adicionando os caracteres da palavra a ser buscada aos índices da lista vazia.|   """
            listcharx.append(word[x])
        
        #print(listx)
        #print (listcharx)

        """"   |Tamanho palavra|     """
        lenx = int(len(listx))

        """"     |Lista Cos0 Y|      """
        for y in range (0, len(endlist), 1):
            """"   |Adicionando os valor 0 aos índices da lista vazia.|   """
            listy.insert(y, int(0))
            """"   |Se o valor dentro do índice for igual ao valor em >listcharx<, substitui o valor por 1.|   """
            for x in listcharx:
                if x in endlist[y]:
                    listy.insert(y, int(1))
                    """"   |Remove o último índice da lista(lixo de informação).|   """
                    listy.pop()

        #print(listy)
        print("Procurando palavras com {} de similaridade.".format(sm))
        for z in range (0, len(listy), 1):
            if  int(z)+int(len(listx)) <= int(len(listy)):
                cs = cosine_similarity([listx], [listy[z:lenx]])[0][0]
                print(listx)
                print(listy[z:lenx])
                if float(cs) >= float(sm):
                    cont = cont+1
                    #print(cs,";", cont)
            if lenx < len(listy):
                lenx = lenx+1

        print (cont, "similaridades encontradas!")

if (__name__) == "__main__":    
    Search('').ctrlF()        