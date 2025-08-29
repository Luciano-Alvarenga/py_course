#Escreva um programa para aprovar empréstimo bancário para a compra de um casa. O programa vai perguntar o valor da
#casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode excerder 30% do salário ou então o empréstimo será negado.

house_value = float(input('Qual é o valor da casa R$ '))
salary_worker = float(input('Digite o salário do trabalhador R$ '))
years = int(input('Digite em quantos anos de finaciamento? '))

mouth = years * 12
instalment = house_value / mouth
limit = salary_worker * 0.30

print(f'Para pagar a casa de {house_value:.2f} em {years} anos')
print(f'A prestação será de {instalment:.2f}')

if instalment <= limit:
    print('Emprestimo aprovado')
else:
    print('O emprestimo negado, a prestação excede 30% do salário.')