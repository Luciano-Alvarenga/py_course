#Refaça o desafio 051, lendo o primeiro termo e razão de uma PA, mostrando os 10 primeiros termos da progressão
#usando a estrutura while.

print('-=-' * 10)
print(' 10 TERMOS DE UMA PA')
print('-=-' * 10)

first = int(input('Digite o termo: '))
reason = int(input('Digite a razão: '))

count = 1
term = first

while count <= 10:
    print(f'{term}', end=' → ')
    term += reason
    count += 1

print('FIM...')
