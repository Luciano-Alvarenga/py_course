#Escreva um programa que leia a velocidade de um carro.
#Se eu ele ultrapassar 80km/h, mostre uma mensagem que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.
# Lê a velocidade do carro.

speed = float(input('Digite a velocidade do carro em (Km/h): '))
if speed > 80:
    excess = speed - 80
    traffic_fine = (speed-80) * 7
    print(f'Você foi multado! Pois ultrapassou o limite da via que é 80km/h! ')
    print(f'Você ultrapassou o limite em {excess:.0f} Km/h')
    print(f'O valor da multa será de R${traffic_fine:.2f}')
else:
    print('Tudo certo! Você está dentro do limite de velocidade!')