#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Vitoria".
city = input('Em que cidade você nasceu? ').strip().title()

print('Iremos analisar se a cidade começa com a palavra: Vitoria')

if city.startswith('Vitoria'):
    print('Sim, a sua cidade começa com a palavra Vitoria.')
else:
    print('A sua cidade não começa com a palavra Vitoria.')





''''city = str(input('Em que cidade você nasceu? ').strip().title())
print ('Iremos analisar se a cidade começa com a palavra: ')
x = 'Vitoria' in city[0]
if x == True: print ('Sim a sua cidade começa com a palavra Vitória')
else: print ('A sua cidade não começa com a palavra Vitória')'''

#Jeito do professor Guanabara
'''cid = str(input('Em que cidade você nasceu? ')).strip()
print (cid[:5].upper() == 'Vitoria')'''

''''city = str(input('Em que cidade você nasceu? ').strip())
print (f'cid antes: {cid}')
city = cid.upper().startswith()
print (f'cid depois: {cid}')
print ('Iremos analisar se a cidade começa com a palavra: ')
x = 'Vitoria' in cid[0].title()
print (f'title:{cid[0].title()}')
if x == True: print ('Sim a sua cidade começa com a palavra Vitória')
else: print ('A sua cidade não começa com a palavra Vitória')'''