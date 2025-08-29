#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares, euro e libras ela pode comprar.
#considere Dólar U$ 5.89, Euro € 6.70, Libra £ 7.00.
real = float(input('Quanto de dinheiro você tem na carteira? R$: '))
dollar = real / 5.89
euro = real / 6.70
pound = real / 7
print(f'Com R${real:.2f} você pode comprar US${dollar:.2f} \nCom R${real:.2f} você pode comprar €{euro:.2f} \nCom R${real:.2f} você pode comprar £{pound:.2f}')