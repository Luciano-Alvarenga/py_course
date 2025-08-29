#Crie um programa que leia o preço de vários produtos. O programa deverá perguntar se o usuário vai
#continuar.
#No final mostre:
#A) Qual o total gasto na compra.
#B) Quantos produtos custam mais de R$ 1000.
#C) Qual é o nome do produto mais barato.

plus_1000 = 0
cheap_price = None
cheap_name = ''
total_price = 0

print('=' * 18)
print('Lojas Alvarenga')
print('=' * 18)
while True:
    name = input('Digite o nome do produto: ')
    price = float(input('Digite o valor do produto: '))

    total_price += price

    if price > 1000:
        plus_1000 += 1

    if cheap_price is None or price < cheap_price:
        cheap_price = price
        cheap_name = name

    cont = input('Deseja continuar? [S/N]: ').strip().upper()
    while cont not in ['S','N']:
        cont = input('Entrada invalida. Deseja continuar? [S/N]: ').strip().upper()

    if cont == 'N':
            break

print('\n====== Resumo da compra =======')
print(f'A) Total gasto na compra: R${total_price:.2f}')
print(f'B) Produtos que custam mais de R$1000: {plus_1000}')
print(f'C) O produto mais barato: {cheap_name} \nCustando: R${cheap_price:.2f}')
