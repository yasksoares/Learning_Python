a = 'A'
b = 'B'
c = 1.1
string = ('a = {} b = {} c = {:.2f}')
string_2 = ('a = {nome1} b = {nome2} c = {nome3:.2f}')
string_3 = ('a = {0} b = {1} c = {2:.3f}')

# erro: out of range: você está buscando algo que acabou

formato = string.format(a, b, c) # isso é um argumento
formato_2 = string_2.format(
    nome1 = a, nome2 = b, nome3 = c) 
formato_3 = string_3.format(a,b,c)

print(formato)
print(formato_2)
print(formato_3)

# Tudo em python é um objeto
# índice = tudo que te uma ordem, sempre começa no zero

nome = 'Yasmim'
idade = 19
formato = '{n} tem {i} anos'
print(formato.format (n= nome, i = idade))

# não é possível utilizar o + para concatenar int e str