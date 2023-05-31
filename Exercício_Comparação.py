primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um valor: ')

if primeiro_valor > segundo_valor:
    print(f'O {primeiro_valor =} é maior do que {segundo_valor =}')
elif primeiro_valor < segundo_valor:
    print(f'O {segundo_valor =} é maior que {primeiro_valor =}')
else:
    print('Os valores são iguais.')