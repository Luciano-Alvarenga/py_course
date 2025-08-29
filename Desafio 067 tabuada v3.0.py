#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
#usuário. O programa será interrompido quando o número solicitado for negativo.

from time import sleep

while True:
    number = int(input('Digite o número para ver a tabuada [digite um valor negativo para sair]: '))

    if number < 0:
        print('Programa encerrado obrigado')
        break

    print(f'Tabuada do número {number}')
    print('Analisando...')
    sleep(1)

    count = 0
    while count < 11:
       result = number * count
       print(f'{number} x {count} = {result}')

       count += 1

    print('-' * 30)
