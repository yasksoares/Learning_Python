# operador in e not in
# strings são iteráveis
# 0 1 2 3 4 5 
# y a s m i m
#-6-5-4-3-2-1

nome1 = 'Yasmim'
print(nome1[0])
print(nome1[1])
print(nome1[2])
print(nome1[3])
print(nome1[4])
print(nome1[5])

nome = input('Digite seu nome: ')
encontrar = input('Digite o que quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else: 
    print(f'{encontrar} não está em {nome}')

print('a' in nome)
print('z' in nome)
print('Yas' in nome)
print('vio' not in nome)

variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)