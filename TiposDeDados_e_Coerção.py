#Tipo int e float
# int -> número inteiro
# o tipo int representa qualquer número
# positivo ou negativo, int sem sinal é considerado positivo

print(11) 
print(-11)
print(0)

# float -> número com ponto flutuante
# o tipo float representa qualquer número
# positivo ou negativo com ponto flutuante, float sem sinal é considerado positivo

print(1.1, 10.11)
print(0.0, -1.5)

# a função type mostra o tipo que  Py inferiu ao valor

print(type('Gabriele'))
print(type(32.9))
print(type(1.1), type(-6.7), type(14), type(-25))

# Tipo de dado bool (boolean)
# Ao questionar algo em um programa, só existem 2 respostas possíveis:
# Sim(true) ou não(false)
# Existem vários operadores para "questionar"
# Dentre eles o ==, que é um operador lógico que questiona se um
# valor é igual ao outro

print(10 == 10) # Sim => True (Verdadeiro)
print(10 == 11) #Não => False (Falso)
print(type(10 == 10))
print(type(True))
print(type(False))

# cnversão de tipos, coerção
# type conversion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos
# str, float, int, bool

print(1 + 1) 
print('a' + 'b')
print(int('3'), type(int('3')))
print(int('3') + 1)
print(type(float('4') + 4.8))
print(int('4') + 13.9)

# uma string vazia é considerada False
print(bool(''))
print(bool(' '))
print(str(11) + 'x')