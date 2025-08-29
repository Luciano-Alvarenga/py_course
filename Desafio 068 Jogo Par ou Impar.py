#Faça um programa que jogue PAR ou Impar com o computador. O jogo só será interrompido quando o jogador
#perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
from time import sleep


print('=' * 26)
print('Vamos jogar PAR ou Impar.')
print('=' * 26)

victory = 0

sleep(0.8)
while True:
    player = int(input(f'Digite um valor: '))
    choice = input('Par ou Impar? [P/I]: ').strip().upper()

    while choice not in ['P','I']:
        choice = input('Escolha inválida. Par ou Impar [P/I]: ').strip().upper()

    computer = random.randint(0,10)
    total = player + computer
    result = 'P' if total % 2 == 0 else 'I'

    print('=' * 56)
    print(f'Você jogou: {player} e o computador jogou: {computer}. Total: {total} ->',end= ' ')
    print(f'PAR' if result == 'P' else 'IMPAR')
    print('=' * 56)

    if choice == result:
        print(f'{"Você venceu!":^56}\n')
        victory += 1
        sleep(0.8)

    else:
        print(f'{"Você perdeu!":^56}')
        break

print(f'Vitórias consecutivas: {victory}')
