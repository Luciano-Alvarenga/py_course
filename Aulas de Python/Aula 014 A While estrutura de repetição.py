#Estrutura de repetição com iteração do usuário.
r = 'S'
while r == 'S':
    person = str(input('Digite o nome: '))
    r = str(input('Você quer continuar [S/N]: ')).upper()
print('Acabou')