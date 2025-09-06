# Crie um programa que tenha uma tupla única com nome de produtos e seus respectivos preços, na sequência.
# No final mostre uma linguagem de preços, organizando os dados em forma tabular.

produtos = ('feijão', 15, 'arroz', 25, 'café', 35, 'açucar', 5, 'sal', 4)

print('-' * 40)
print(f'{"Listagem de preços":^40}')
print('-' * 40)

for pos in range (0, len(produtos), 2):
    name = produtos[pos]
    price = produtos[pos + 1]
    print(f'{name:.<30} R${price:>7.2f}')

    print('-' * 40)