#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
#encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for number in range(1, 501, 2):
    if number % 3 == 0:
    #sintase antiga
    #cont = cont + 1
    #soma = soma + number

    #Abaixo a sintase nova(moderna)
     cont += 1
     soma += number

print(f'A soma de todos os {cont} números solicitados é {soma}')
