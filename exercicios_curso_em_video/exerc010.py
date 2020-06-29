# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
dinheiro = float(input('Insira o valor em reais que você possui R$'))
print('Você poderá comprar ${} dólares.'.format(dinheiro/5))
