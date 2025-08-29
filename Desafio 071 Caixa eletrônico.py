#Crie um programa que simule o funcinamento de um caixa eletrônico. No incio, pergunte ao usuário qual
#será o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor seram
#entregues.

#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10, R$1.

print('=' * 30)
print('{:^30}'.format('Caixa Eletrônico'))
print('=' * 30)


amount = int(input('Qual o valor a ser sacado?: '))

bill = 50
bill_count = 0

while True:
    if amount >= bill:
        amount -= bill
        bill_count += 1

    else:
        if bill_count > 0:
            print(f'{bill_count} cédula(s) R${bill}')

        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1
        elif bill == 1:
            bill = 1
        bill_count = 0
        if amount == 0:
            break