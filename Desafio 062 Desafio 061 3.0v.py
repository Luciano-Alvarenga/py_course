#Melhore o desafio 061, perguntando ao usuário se ele quer mostrar mais alguns termos. O programa encerra quando
#ele disser que quer mostrar 0 termos.


print('-=-' * 10)
print('10 TERMOS DE UMA PA')
print('-=-' * 10)

first = int(input('Digite o termo: '))
reason = int(input('Digite a razão: '))

term = first
count = 1
total = 0
more = 10

while more != 0:
    total = total + more
    while count <= total:
        print(f'{term}', end=' → ')
        term += reason
        count += 1
    print('PAUSA')
    more = int(input('Quantos termos você gostaria de mostrar a mais?  '))
print('FIm...')
