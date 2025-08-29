#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.
phrase = input('Digite o seu nome: ').strip()
phrase.lower()
amount_a = phrase.count('a')
first_position = phrase.find('a')
last_position = phrase.rfind('a')
print(f'A letra "A" aparece {amount_a} vezes.')
print(f'A primeira ocorrência de "A" está na posição {first_position + 1}')
print(f'A última ocorrência de "A" está na posição {last_position + 1}')