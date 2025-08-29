#Melhoro o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
#tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
number_computer = randint(0, 10)

print('-=-' * 20)
print('Sou seu computador... Acabei de pensar em um número entre 0  e 10...')
print('Será que você consegue advinhar qual foi? ')
print('-=-' * 20)

got_it_right = False
attempts = 0

while not got_it_right:
    guess = int(input('Diigite o seu palpite: '))
    attempts += 1
    if guess == number_computer:
        got_it_right = True
    else:
     if guess < number_computer:
      print('Mais... tente mais uma vez')
     elif guess > number_computer:
       print('Menos... tente mais uma vez')

print(f'Você acertou com {attempts} tentativas parábens!')
