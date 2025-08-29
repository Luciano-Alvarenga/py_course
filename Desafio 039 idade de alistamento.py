#Faça um programa que leia o ano de nascimento de um jovem e infome, de acordo com sua idade:
# - Se ele ainda vai se alistar no serviço militar.
# - Se é a hora de se alistar.
# - Se já passou o tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
#Em que ano ele deveria ter se alistado.

from datetime import date

today = date.today().year
born_year = int(input('Digite o ano de nascimento: '))
age = today - born_year

print(f'Quem nasceu em {born_year}, tem {age} anos em {today}')
if age < 18:
    balance = 18 - age
    print(f'Ainda faltam {balance} anos para você se ALISTAR!')
    year = born_year + 18
    print(f'O ano que você deverar se ALISTAR será em {year}')

elif age == 18:
    print('Você deve se ALISTAR IMEDIATAMENTE!')

elif age > 18:
    balance = age - 18
    print(f'Você já deveria ter se ALISTADO a {balance} anos!')
    year = born_year + 18
    print(f'O ano que você deveria ter se ALISTADO foi em {year}.')
