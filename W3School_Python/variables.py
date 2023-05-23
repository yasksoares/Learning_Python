if 5 > 2:
    print("Five is greater than two)")

# em py os códigos são por blocos

x = 10
y = "Hello, World"
print(y)
print(x)

""""
This is a multiline comment

"""

# Variables are a pot of data

x, y, z = 'juice', 'water', 'refri' #um valor para várias variáveis
print(x)
print(y)
print(z)

a = 'Python is cool'
print(a)

""""
A função print geralmente é usada para variáveis de saída
"""

c = 'Python '
d = 'is '
e = 'funny'
print(c + d + e)

# também é possível utilizar uma vírgula

alfa = 8
omega = 7
print(alfa + omega)

# com varíaveis armazenando números, o + serve como operador matemático

f = 'John has'
g = 15
h = 'years old'
print(f, g, h)

"""
Ao misturar variáveis de strings e números, o operador + não funciona, 
é necessário usar a vírgula
Também não é preciso colocar uma separação de espaço na varíavel,
ela faz isso automaticamente 

"""

# Todas as variáveis criadas até aqui foram variáveis globais

x = 'amazing'

def myFunction():
  x = 'beautiful'
  print('Mary is ' + x)

myFunction()

print('Anna is ' + x)
  
# para usar a variável contida dentro de uma função, basta usar a função global

def my_function():
   global l 
   l = '99 years old'
   print('My grandmother has ' + l)
my_function()

print('I have ' + l)

# Did you see? It's easy. Let's continue

m = 45 

def MyFunction():
   global m
   m = 25
   n = 'miles'
   print('I walked', m, n)

MyFunction()

# to chance a variable, you can use a global function inside another function


