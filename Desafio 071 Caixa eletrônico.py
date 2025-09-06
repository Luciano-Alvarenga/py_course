#Crie um programa que simule o funcinamento de um caixa eletrônico. No incio, pergunte ao usuário qual
#será o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor seram
#entregues.

#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10, R$1.

print('=' * 30)
print('{:^30}'.format('Caixa Eletrônico'))
print('=' * 30)

amount = int(input('Qual o valor a ser sacado?: '))

banknote = 50
banknote_count = 0

while True:
    if amount >= banknote:
        amount -= banknote
        banknote_count += 1

    else:
        if banknote_count > 0:
            print(f'{banknote_count} cédula(s) R${banknote}')

        if banknote == 50:
            banknote = 20
        elif banknote == 20:
            banknote = 10
        elif banknote == 10:
            banknote = 1
        elif banknote == 1:
            banknote = 1
        banknote_count = 0
        
        if amount == 0:
            break