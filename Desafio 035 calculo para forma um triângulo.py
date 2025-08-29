#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#Exemplos usar as três variaveis de baixo como retas.
#r1
#r2
#r3

print('-=-' *20)
print('Informe o comprimento da três retas.')
print('-=-' * 20)

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas podem forma um triângulo. 🔺')

else:
    print('As retas não podem forma um triângulo. ❌')