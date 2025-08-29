#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50 por,
# km para viagens de ate 200km e R$0.45 para viagens mais longas.

distance = float(input('Qual é a distância da sua viagem em (Km)? '))
print (f'Você está prestes a começar uma viagem de {distance:.1f}Km')

if distance <=200:
    price = distance * 0.50
else:
    price = distance * 0.45

print(f'O preço da passagem será de R${price}')