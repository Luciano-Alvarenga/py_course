#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Exemplo: Ana Maria dos Santos
#Primeiro nome: Ana
#Segundo nome: Santos
name = input('Digite o seu nome completo: ').strip()
name_parts = name.split()
if len(name_parts) >= 2:
    first_name = name_parts[0]
    last_name = name_parts[-1]
else:
    first_name = name_parts[0]
    last_name = name_parts[-1]

print (f'Prazer em conhece-la: {name}')
print (f'Seu primeiro nome é: {first_name}')
print (f'Seu último nome é: {last_name}')