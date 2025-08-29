#A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
#categoria, de acordo com a idade:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 20 anos: Sênior
# - Acima: Master

athlete = int(input('Digite a idade do atleta: '))
if athlete <= 9:
    print('Categoria MIRIM')

elif athlete <= 14:
    print('Categoria INFANTIL!')

elif athlete <= 19:
    print('Categoria JUNIOR!')

elif athlete == 20:
    print('Categoria SÊNIOR')

elif athlete > 20:
    print('Categoria MASTER!')
