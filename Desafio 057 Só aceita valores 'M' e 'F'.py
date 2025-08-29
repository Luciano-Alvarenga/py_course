#Faça um programa que leia o sexo de uma pessoa, mas só aceite valores 'M' ou 'F'. Caso esteja errado, peça para
#digitar novamente até ter um valor cerreto.

sex = ''

while sex not in ['M', 'F']:
   sex = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
   if sex not in ['M', 'F']:
       print('Valor invalido tente novamente!')
if sex == 'M':
    print('Você é HOMEM!')
else:
    print('Você é MULHER!')
