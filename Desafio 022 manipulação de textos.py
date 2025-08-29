#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas.
#O nome com todas as letras minúsculas.
#Quantas letras ao todo(sem considerar espaços)
#Quantas letras tem o primeiro nome.
nome = str(input('Digite o seu nome completo: ')).strip()
print ('Analisando o seu nome...')
print ('Seu nome em letras maiúsculas: {}'.format(nome.upper()))
print ('Seu nome em letras minúsculas: {}'.format(nome.lower()))
print ('Seu nome tem ao todo {} letras.'.format (len(nome) - nome.count(' ')))
print ('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))