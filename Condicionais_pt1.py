# if / elif / else
# se / se nao se / se nao

entrada = input ('Você quer "entrar" ou "sair"?')
acesso = input('Digite seu acesso: ')
entrada = entrada.lower() # o .lower serve para aceitar varias formas de entrada da mesma str

if entrada == 'entrar':
    print('Você entrou no sistema')
    print(f'Seu código de acesso é: {acesso}')
    print('Boa navegação!')
elif entrada == 'sair':
    print('Você saiu do sistema')
    print('Até logo!')
else:
    print('Você não digitou uma correspondência válida.')
