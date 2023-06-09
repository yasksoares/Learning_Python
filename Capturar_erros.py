"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algu erro ao tentar executar
"""
# print(123)
# print(456)
# int('a') vai retornar um erro

# estourar uma exceção, significa que vai aparecer um erro

numeroS = input('Vou dobrar o número que você digitar: ')

try:
    print('STR:', numeroS)
    numeroF = float(numeroS)
    print('FLOAT:', numeroF)
    print(f'O dobro de {numeroS} é {numeroF * 2}')
except:
    print('Isso não é um número')

# considera apenas números inteiros

if numeroS.isdigit():
    numeroF = float(numeroS)
    print(f'O dobro de {numeroS} é {numeroF * 2}')
# é necessário tratar o input do usuário
else:
    print('Isso não é um número')



