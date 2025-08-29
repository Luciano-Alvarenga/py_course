#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 0
#até 10, com pausa de 1 segundo entre eles, por emotion de fogos.

import time
for number in range(10, -1, -1):
    print(number)
    time.sleep(1)
print('🎆🎇 BOOM! Fogos de artifício! 🎉✨')