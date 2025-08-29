#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
#valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
#(desconsiderando o flag).

number = 0
count = 0
soma = 0

while True:
    number = int(input('Digite o número [999 para parar]: '))
    if number == 999:
        break
    count += 1
    soma += number

print(f'Você digitou {count} números e a soma entre eles é {soma}')