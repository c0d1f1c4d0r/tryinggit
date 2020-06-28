"""Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informações possíveis sobre ele."""

informacao = input('Digite alguma coisa: ')
print('O tipo primitivo da informação digitada é ', type(informacao))
print('A informação digitada contém apenas espaços? ', informacao.isspace())
print('A informação digitada contém apenas números? ', informacao.isnumeric())
print('A informação digitada contém apenas caracteres alfabéticos? ', informacao.isalpha())
print('A informação digitada é alfa numérica? ', informacao.isalnum())
print('A informação digitada está em maiúsculas? ', informacao.isupper())
print('A informação digitada está em minúsculas? ', informacao.islower())
print('A informação digitada está capitalizada? ', informacao.istitle())
