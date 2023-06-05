# Operadores Lógicos
# and (e), or (ou), not (não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira
# Se qualquer valor for considerado verdadeiro, a expressão inteira
# será avaliada naquele valor
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o None que é usado para representar um não valor


# entrada = str(input ('[E]ntrar [S]air: '))
# senha_digitada = input('Senha: ')
# senha_permitida = '123456'

# # quanto mais condição tiver no if, mais complciado vai ficar o código
# # tudo que é posto entre () é avaliado primeiro
# # é usado () para não haver ambiguidade

# if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# avaliação de curto circuito)
senha = (True or False or 0 or 'abc')
print(senha)
senha1 = input('Senha: ') or 'Sem senha'
print(senha1)
