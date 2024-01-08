from items import*
import time

class Minterms(Term):
    """ ||| Armazenar expressões. ||| """

    def __init__(
        self, minterms=None, not_cares=None,
    ):
        if minterms is None:
            minterms = []
        if not_cares is None:
            not_cares = []

        self.minterms = minterms
        self.not_cares = not_cares


    def simplify(self):
        prime_implicants = find_prime_implicants(self.minterms, self.not_cares)
        result = find_essential_prime_implicants(prime_implicants, self.minterms)
        #print(result)
        result = '+'.join(map(str, result))
        result = list(result)
        #print(result)
        resultF = ''
        c = 0
        for x in result:
            if c == 0:
                resultF = resultF + "("
                if x == '1':
                    resultF = resultF + 'A'
                    c = c+1
                elif x == '*':
                    c = c+1
                else:
                    resultF = resultF + "A'"
                    c = c+1
            elif c == 1:
                if x == '1':
                    resultF = resultF + 'B'
                    c = c+1
                elif x == '*':
                    c = c+1
                else:
                    resultF = resultF + "B'"
                    c = c+1
            
            elif c == 2:
                if x == '1':
                    resultF = resultF + 'C'
                    c = c+1
                elif x == '*':
                    c = c+1
                else:
                    resultF = resultF + "C'"
                    c = c+1
            
            elif c == 3:
                if x == '1':
                    resultF = resultF + 'D'
                    c = c+1
                elif x == '*':
                    c = c+1
                else:
                    resultF = resultF + "D'"
                    c = c+1
            
            else:
                resultF = resultF + ")" + " + "
                c = 0
            
        resultF = resultF + ")"
        word = ('\033[35m Expressões simplificadas: \033[m\n')

        for x in range(0, len(word), 1):
            print(word[x], end='', flush = True)
            time.sleep(0.10)

        print("-"*50)

        for x in range(0, len(resultF), 1):
            print(resultF[x], end='', flush = True)
            time.sleep(0.10)

        #print(resultF + ")")
    


if __name__ == "__main__":
    ''' || List with items that make up the truth table. || '''
    t = ['0 0 0 0', '0 0 0 1', '0 0 1 0', '0 0 1 1', '0 1 0 0', '0 1 0 1', '0 1 1 0', '0 1 1 1', '1 0 0 0', '1 0 0 1', '1 0 1 0', '1 0 1 1', '1 1 0 0', '1 1 0 1', '1 1 1 0', '1 1 1 1']
    tkmap = {0: '0000', 1: '0001', 2: '0010', 3: '0011', 4: '0100', 5: '0101', 6: '0110', 7: '0111', 8: '1000', 9: '1001', 10: '1010', 11: '1011', 12: '1100', 13: '1101', 14: '1110', 15:'1111'}
    ''' || Expressions resulting from every possible positive truth table output. || '''
    expressions = {0:"(A'B'C'D')", 1:"(A'B'C' D)", 2:"(A'B' C D')", 3:"(A'B' CD)", 4:"(A'B' CD)", 5:"(A' B C'D')", 5:"(A' B C' D)", 6:"(A' BC D')", 7: "(A' BCD)", 8: "(A B'C'D')", 9: "(A B'C' D)", 10: "(A B' C D')", 11: "(A B' CD)", 12: "(AB C'D')", 13: "(AB C' D)", 14: "(ABC D')", 15: "(ABCD)"}

    c = 0
    result = ''
    kmap = ''
    output = []

    print("\033[32mA B C D S\033[32m")

    ''' || Loop que exibirá os itens da tabela verdade formatados. || '''
    for x in t:
        print(x,'',end = '')
        i = input()
        x = x+' '+ i
        output.append(x)

    ''' || Loop que exibirá os itens da tabela verdade formatados. || '''
    for x in output:
        if x[8:] == '1':
            result = result + expressions[c] + '+'
            kmap = kmap + ' ' + tkmap[c]
            
        c = c+1
    
    c = 0

    cc = 0

    result = result[:-1]
    kmap = kmap.split()
    kmaps = t

    liste = []

    cc = int(input("Add irrelevant term? Y(0)|N(1):\n"))

    while cc == 0:
        print("\033[28mTerms:\033[28m")
        for x in kmaps:
            print(x)
        print("Irrelevant terms: ")
        for x in liste:
            print(x)
        not_care = input("\nIrrelevant term: ")              
        liste.append(not_care)

        for x in kmaps:
            if x == not_care:
                kmaps.remove(x)

        cc = int(input("Add other term? Y(0)|N(1):\n"))
    

    print("\033[33mBoolean expression: \033[m", result)

    str_terms = kmap
    #print(str_terms)
    terms_not_care = liste
    t_minterms = [Term(term) for term in str_terms]
    not_cares = [Term(term) for term in terms_not_care]

    minterms = Minterms(t_minterms, not_cares)
    minterms.simplify()
