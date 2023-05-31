# Calcular usando Bhaskara

A = float(input('Digite o valor de a: ')) 
B = float(input('\nDigite o valor de b: '))
C = float(input('\nDigite o valor de c: '))
delta = float((B **2) - (4*A*C))

if delta <= 0:
    print('A equação não possui resultado real.')
elif A == 0:
    print('Valor indeterminado')
elif B == 0 or C == 0:
    print('Insira valores diferentes de 0 para B e C.')
else:
    x1 = (-B + (delta ** 0.5))/(2 * A)
    x2 = (-B - (delta ** 0.5))/(2 * A)
    print(f"\nO valor de x' é: {x1:.3f}\n")
    print(f"O valor de x'' é: {x2:.3f}")
