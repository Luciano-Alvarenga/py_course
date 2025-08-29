#Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep

print('-=-' * 11)
print('Vamos jogar "JO KEN PÔ"')
print('-=-' * 11)

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computer = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

try:
    player = int(input('Qual é a sua jogada? '))
    if player not in [0, 1, 2]:
        raise ValueError("Jogada inválida!")

    print('-=-' * 3)
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ!!!')
    sleep(1)
    print('-=-' * 3)

    print('-=-' * 10)
    print(f'O computador jogou {itens[computer]}')
    print(f'O jogador escolheu {itens[player]}')
    print('-=-' * 10)

    if computer == player:
        print('Empate!')
    elif (player == 0 and computer == 2) or \
         (player == 1 and computer == 0) or \
         (player == 2 and computer == 1):
        print('Jogador venceu!')
    else:
        print('Computador venceu!')

except (ValueError, IndexError):
    print('Jogada inválida! Escolha 0, 1 ou 2.')


'''import random


def jogar_jokenpo():
    opcoes = ['pedra', 'papel', 'tesoura']

    print("Vamos jogar Jokenpô!")
    print("Escolha: pedra, papel ou tesoura")

    jogador = input("Sua escolha: ").lower()
    while jogador not in opcoes:
        print("Escolha inválida.")
        jogador = input("Escolha novamente (pedra, papel ou tesoura): ").lower()

    computador = random.choice(opcoes)

    print(f"\nVocê escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == 'pedra' and computador == 'tesoura') or \
            (jogador == 'papel' and computador == 'pedra') or \
            (jogador == 'tesoura' and computador == 'papel'):
        print("Você venceu!")
    else:
        print("Você perdeu!")


# Executa o jogo
jogar_jokenpo()'''
