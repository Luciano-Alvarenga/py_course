#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Vitoria".
#Jeito atual de fazer.
city = input('Em que cidade você nasceu? ').strip()
print (f'city {city}')

city = city.upper()
print (f'city upper:{city}')

city = city.replace('Ó','O')
print (f'city replace:{city}')

starts_with_vitoria = city.startswith('VITORIA')
print (f'Starts with VITORIA? {starts_with_vitoria}')