#Crie um programa que leia vários números inteiros pelo teclado. O pragrama só vai para quando o usuário
#digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
#foi a soma entre eles (desconsiderando o flag).

count = 0
total = 0

while True:
    number = int(input('Digite o número [999 para parar]: '))

    if number == 999:
        break
    count += 1
    total += number

print(f'Você digitou {count} números e a soma entre eles é {total}')