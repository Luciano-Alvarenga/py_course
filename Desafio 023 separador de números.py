#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Exemplo: Digite um número: 1987
#unidad:7
#dezena:8
#centena:9
#milhar:1
num = int(input('Digite um número: '))
n = str(num)
print ('Analisando o número {}'.format(num))
print ('Unidade {}'.format(n[3]))
print ('Dezena {}'.format(n[2]))
print ('Centena {}'.format(n[1]))
print ('Milhar {}'.format(n[0]))