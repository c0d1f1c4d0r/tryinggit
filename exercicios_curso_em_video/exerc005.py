# Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Insira um número: '))
print('O número inserido foi {} seu antecessor é {} e seu sucessor é {}.'.format(n, (n-1), (n+1)))
