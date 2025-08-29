#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
#perguntar se o usuário quer ou não continuar.
#No final mostre:

#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos.


over_18 = 0
men = 0
under_20 = 0

while True:
    print('=' * 28)
    age = int(input('Digite a sua idade: '))

    print('=' * 28)
    sex = str(input('Digite o seu sexo [M,F]: ')).strip().upper()


    while sex not in ['M', 'F']:
        print('=' * 44)
        sex = input('Entrada inválida. Digite novamente [M/F]: ').strip().upper()

    if age > 18:
      over_18 += 1

    if sex == 'M':
      men += 1

    if age < 20:
      under_20 += 1

    print('=' * 28)
    cont = input(f'Deseja continuar [S/N]: ').strip().upper()

    while cont not in ['S', 'N']:
        print('=' * 28)
        cont = input('Entrada invalida. Deseja continuar [S/N]: ').strip().upper()

    if cont == 'N':
        break

print('=' * 46)
print(f'A) Total de pessoas com mais de 18 anos: {over_18}')
print(f'B) Total de homens cadastrados: {men}')
print(f'C) Total de mulheres com menos de 20 anos: {under_20}')
print('=' * 46)
