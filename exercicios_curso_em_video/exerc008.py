# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Insira um valor em metros: '))
print('O valor {} metros é igual a {} centímetros ou a {} milímetros.'.format(metros, (metros/100), (metros/1000)))
