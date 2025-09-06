# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o número nove.
# B) Em que posição foi digitado o número 3.
# C) Quais foram os números pares.

def soma(a,b):
    addtion = abs(a+b)
    return addtion

if __name__ == '__main__':
    print('Soma de números')

    number_1 = float(input('Digite um primeiro valor: '))
    number_2 = float(input( 'Digite um segundo valor: '))

    plus = soma(number_1, number_2)

    print(f'A soma entre {number_1} e {number_2} = {plus}')
