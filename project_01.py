print("Exemplo 1: Hello, world")

if (5 > 2):
    print("Exemplo 2: Five is greather than two!") # após o if é necessário ":"

"""
Para fazer comentários multilinhas,
é necessário usar esse formato
"""

# cada linha é um bloco em py
# variáveis são recipientes para armazenar valores de dados

x = 4
print("Exemplo 3: x =", x)

# por não ter uma função definida, o exemplo acima deve ser separada em blocos
# é possível especificar o tipo de dado usando:

y = int(5)
print("Exemplo 4:", y)

z = 89
print("Exemplo 5:", (float(z)))

# no exemplo acima está sendo indicado o tipo de dado dentro da função print

a, b, c = "orange", "apple", "banana"
print("Exemplo 6:", a)
print("Exemplo 6:", b)
print("Exemplo 6:", c)

# no exemplo acima, foi usado 3 variáveis armazenando 3 dados, um em cada

e = f = g = "Sugar"
print("Exemplo 7:", e)
print("Exemplo 7:", f)
print("Exemplo 7:", g)

#acima tem-se um valor para 3 variáveis

fruits = ["maçã", "banana", "laranja", "goiaba"]
a_1, b_1, c_1, d_1 = fruits
print("Exemplo 8:", a_1)
print("Exemplo 8:", b_1)
print("Exemplo 8:", c_1)
print("Exemplo 8:", d_1) 

# acima temos uma descompactação de uma lista

x_1 = "Python "
y_1 = "is "
z_1 = "awesome"
print("Exemplo 9:", x_1 + y_1 + z_1)



