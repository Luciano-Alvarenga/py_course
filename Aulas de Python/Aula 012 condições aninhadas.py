name = str(input('Digite um nome? ')).strip().title()
if name == 'Luciano':
    print(f'Seu nome é tão lindo, {name}!')

elif name in ['Diego', 'Lais', 'Antonio']:
    print(f'Você é família, {name}!')

elif name in 'Suzy_Martins Ana_Paula Fran Jaqueline_Andrade':
    print('É só pra comer e sair fora, inclusive o cú!')

else:
 print('Seu nome é normal!')
print(f'Tenha um bom dia, {name}!')