from time import sleep

number_1 = float(input('Digite o o primeiro valor: '))
number_2 = float(input('Digite o segundo valor: '))
options = 0

while options != 5:
    print('=' * 20)
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] NÚMERO MAIOR
[4] NOVOS NÚMEROS
[5] SAIR''')
    print('=' * 20)

    print('=' * 30)
    options = int(input('Escolha uma das opções: '))
    print('=' * 20)


    if options == 1:
        plus = number_1 + number_2
        print(f'A soma entre {number_1} e {number_2} = {plus}')

    elif options == 2:
        multiplication = number_1 * number_2
        print(f'A multiplicação entre {number_1} e {number_2} = {multiplication}')

    elif options == 3:
        if number_1 >number_2:
            greater_number = number_1

        elif number_2 > number_1:
            greater_number = number_2

        else:
            print(f'Ambos os números são iguais {number_1}')
            continue

        print(f'Entre {number_1} e {number_2} o maior número é {greater_number}')

    elif options == 4:
        print('Digite os novos valores.')
        number_1 = float(input('Digite o primeiro valor: '))
        number_2 = float(input('Digite o segundo valor: '))

    elif options == 5:
        print('Finalizando o programa.')