#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
#Que ele analise o ano atual da maquina.

from datetime import date
year = int(input('Qual ano você quer analisar? Coloque 0 para analizar o ano atual: '))
if year == 0:
    year = date.today().year

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'O ano {year} é BISSEXTO!')

else:
    print(f'O ano {year} não é BISSEXTO!')