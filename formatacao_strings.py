nome = 'Yasmim Soares'
altura = 1.74
peso = 72
imc = peso / (altura ** 2)

# IMC = peso / altura²
# variável = ... ( isso retornará Ellypses)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)


# exemplo de :,.Xf
moedas = 145879.85
linha_exemplo = f'{nome} tem {moedas:,.2f} de moedas'
print(linha_exemplo)
