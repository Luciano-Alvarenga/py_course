#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - Á vista dinheiro/cheque: 10% de desconto.
# - Á vista no cartão: 5% de desconto.
# - Em até 2x no cartão: Preço normal.
# - 3x ou mais no cartão: 20% de juros.

product = float(input('Digite o valor dos produtos: '))
print('''[1] Á vista dinheiro/cheque 
[2] Á vista no cartão
[3] 2 x no cartão
[4] 3 x ou mais no cartão''')

options = int(input('Digite qual a opção você deseja: '))


if options == 1:
    final_value = product - (product * 10 / 100)
    print(f'A vista/cheque você vai pagar R${final_value:.2f} com 10% de DESCONTO!')

elif options == 2:
    final_value_2 = product - (product * 5 / 100)
    print(f'Á vista no cartão você vai pagar R${final_value_2:.2f} com 5% de DESCONTO!')

elif options == 3:
    final_value_3 = product / 2
    print(f'Sua compra sera parcelada em 2x de R${final_value_3:.2f} SEM JUROS')
    print(f'Sua compra de R${product} vai sair por R${product:.2f} no final.')

elif options == 4:
    number_4 = product + (product * 20 / 100)
    installments = number_4 / 3
    print(f'Sua compra será parcelada em 3x de R${installments:.2f}')
    print(f'Sua compra de R${product:.2f} vai sair por R${number_4:.2f} com 20% de ACRÉSCIMO!.')

else:
    print('Obrigado pela visita')
