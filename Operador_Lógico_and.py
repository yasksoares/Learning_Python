# Operadores Lógicos
# and (e), or (ou), not (não)
# and - todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira
# seráavaliada naquele valor
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o None que é usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if true
# if condicao: 
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto-circuito
print(True and False and True)
print(bool(0))
print(bool(' '))
print(True and 0 and True)

if 0 and 1:
    print( True and 1) # não será exibido nada, pois apenas o 0 no if representa falsy
