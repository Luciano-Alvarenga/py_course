#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Digite o seu nome completo: ')).upper().strip()
print ('Analisando o nome... {}'.format(nome))
print ('Tem Silva no seu no seu nome? {}'.format('SILVA' in nome))


#Jeito do professor Guanabara
nome = str(input('Qual o seu nome completo: ')).strip()
print ('Analisando o nome... {}'.format(nome))
print ('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))

