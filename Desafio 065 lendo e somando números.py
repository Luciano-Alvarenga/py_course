#Crie um programa que leia vários números inteiros pelo teclado. No final da execução , mostre a média entre todos
#os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
#continuar a digitar valores.

answer = 'Ss'
plus = 0
quantity = 0
media = 0
higher_number = 0
lower_number = 0

while answer in 'Ss':
    number = int(input('Digite um número: '))
    plus += number
    quantity += 1

    if quantity == 1:
        higher_number = lower_number = number
    else:
        if number > higher_number:
            higher_number = number
        if number < lower_number:
            lower_number = number
    answer = str(input('Digite [S] para continuar ou [N] para sair: ')).strip().upper()[0]
    media = plus / quantity

print('=' * 20)
print(f'Você digitou {quantity} números e a média foi {media:.2f}')
print(f'E o maior número foi {higher_number} e o menor número foi {lower_number}')
print('=' * 20)
print('Fim do programa!')
