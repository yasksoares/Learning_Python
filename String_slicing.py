"""
String slicing
0123456789
Olá Mundo
-987654321
Slicing [i:f:p] [::]
obs: the len function returns the number of characters in the str
"""
variable = 'Olá mundo'
print(variable[4:8])

print(variable[4:])

print(variable[4])

print(variable[0:5])

print(variable[0:])

print(variable[-8:-2])

print(variable[3])

print(len(variable[3:8]))

print(variable[0:len(variable):1])

print(variable[0:9:1])
print(variable[0:9:2])
print(variable[0:9:3])

print(variable[::-1])
print(variable[-1:-10:-1])




