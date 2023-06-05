# operador lógico "not"
# usado para inverter expressões 
# not True = False
# not False = True

senha = input('Senha: ')

if senha != '123456':
    print('Senha incorreta')
elif senha == '123456':
    print('Você entrou')
elif not senha:
    print('Você não digitou nada')
else:
    print('Erro')

print (not True)
print (not False)