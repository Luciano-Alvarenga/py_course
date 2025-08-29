# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.
# Seu programa devera ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.

numbers_written = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
                    'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DESSOITO', 'DESSENOVE', 'VINTE')

while True:
    number = int(input('Digite um número entre 0 e 20: '))
    if 0 <= number <= 20:
        print(f'Você digitou o número {numbers_written[number]}')
        break

    print('Entrada inválida. Tente novamente.')