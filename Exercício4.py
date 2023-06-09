"""
Escreva um programa que receba a idade de uma pessoa e exiba 
uma mensagem informando se ela é maior de idade ou não.
"""
idade = int(input('Digite sua idade: '))
maioridade = 18

if idade >= maioridade:
    print('Você é maior de idade')
else:
    print(f'Você não tem {maioridade} ou mais')