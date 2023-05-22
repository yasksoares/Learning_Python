concatenacao = 'A' + 'B' + 'C'
print(concatenacao)

nome = 'Yasmim' + " " + 'Soares'
print(nome)

a_dez_vezes = 'A' * 10 # nesse caso está como uma função de repetição
tres_vezes_yasmim = 'Yasmim' * 3
print(a_dez_vezes)
print(tres_vezes_yasmim)

# 1. (n+n)
# 2. **
# 3. */ // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5 # 7
print(conta_1)

conta_1_2 = (1 + 1) ** (5 + 5)
print(conta_1_2)

conta_2 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_2)

print(conta_1_2 == conta_2)
print(conta_1 == conta_2)
