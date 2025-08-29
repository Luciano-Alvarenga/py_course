#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

#usando comando math importa toda a biblioteca de matemática.
import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print (f'O ângulo de {ângulo} tem o SENO de {seno:.2f}')
cosseno = math.cos(math.radians(ângulo))
print (f'Ó ângulo de {ângulo} tem o COSSENO {cosseno:.2f}')
tangente = math.tan(math.radians(ângulo))
print (f'O ângulo de {ângulo} tem a TANGENTE {tangente:.2f}')

#Executando com o comando from math import radians, sin, cos, tan - você importa coisas especificas da biblioteca de matemática.
from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print(f'O ângulo de {ângulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(ângulo))
print (f'O ângulo de {ângulo} tem o COSSENO {cosseno:.2f}')
tangente = tan(radians(ângulo))
print (f'O ângulo de {ângulo} tem a TANGENTE {tangente:.2f}')