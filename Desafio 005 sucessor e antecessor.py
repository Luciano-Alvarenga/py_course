print('-=-' * 33)
print('Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.')
print('-=-' * 33)
n = int(input('Digite um valor: '))
a = n - 1
s = n + 1
print ('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n, a, s))


#Posso economizar memória usando a variável direto no format no exemplo abaixo.
n = int(input('Digite um valor: '))
print(f'Analisando o valor {n}, seu antecessor é {n-1} e o seu sucessor é {n+1}')