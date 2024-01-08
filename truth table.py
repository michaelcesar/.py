''' || List with items that make up the truth table. || '''
t = ['0 0 0', '0 0 1', '0 1 0', '0 1 1', '1 0 0', '1 0 1', '1 1 0', '1 1 1']

''' || Expressions resulting from every possible positive truth table output. || '''
expressions = {0:"(A'B'C')", 1:"(A'B' C)", 2:"(A' B C')", 3:"(A' BC)", 
                4:"(A B'C')",5:"(A B' C)", 6:"(AB C')", 7:"(ABC)" }

''' || List that will receive the truth table items with their outputs. || '''               
output = []

s = ''
c = 0
result = ''

print("\033[32mA B C S\033[32m")

''' || Loop that will display the formatted truth table items. || '''
for x in t:
    print(x,'',end = '')
    i = input()
    x = x+' '+ i
    output.append(x)

''' || Loop that will check if the truth table outputs are positive. || '''
for x in output:
    if x[6:] == '1':
        result = result + expressions[c] + '+'
    c += 1    
len = len(result)

print("\033[33mBoolean expression: \033[m", result[:len-1])