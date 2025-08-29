#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

number = int(input('Digite um número inteiro: '))
print('''Escolha uma base para conversão:
[1] Para converter para BINÁRIO.
[2] Para converter para OCTAL.
[3] Para converter para HEXADECIMAL.''')

options = int(input('Digite qual das opcões você deseja coverter: '))

if options == 1:
    print(f'O número {number} convertido para BINÁRIO é {bin(number)[2:]}')
elif options == 2:
    print(f'O número {number} convertido OCTAL é {oct(number)[2:]}')
elif options == 3:
    print(f'O número {number} convertido para HEXADECIMAL é {hex(number)[2:].upper()}')

else:
    print('Opção invalida tente novamente!')
