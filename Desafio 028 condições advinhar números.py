#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar,
# descobrir qual foi o número escolhido pelo computador.
#O programa deverar escrever na tela se o usuário venceu ou perdeu.

from random import randint
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente advinnhar...' )
print('-=-' * 20)
number_computer = randint(0, 5)
guess = int(input('Digite o seu palpite: '))
if guess == number_computer:
    print('Você acertou! Parabéns!!!')
else:
    print(f'Você errou. Eu pensei no número {number_computer}! e não no {guess}!')