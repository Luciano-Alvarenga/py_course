#Desenvolva um programa que leia o primeiro termo e a razão de um PA(progressão aritmética. No final, mostre os 10
# primeiros termos dessa progressão.

from tokenize import Number

print('-=-' * 10)
print('   10 TERMOS DE UMA PA')
print('-=-' * 10)

first = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
tenth = first + (10 - 1) * reason
for number in range(first , tenth, reason):
    print(F'{number}', end=' → ')

print('ACABOU!!!')