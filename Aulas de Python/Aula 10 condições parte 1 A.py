#Condição normal.
tempo = int(input('Quantos anos tem o seu carro? '))
if tempo<=3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho ')
print('--fim--')

#Condição simplificada.
tempo = int(input('Quantos anos tem o seu carro: '))
print('Seu carro é novo'if tempo<=3 else'Seu carro é velho')
print('--fim--')