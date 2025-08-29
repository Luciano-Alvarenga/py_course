# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem
#de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

soccer_table = ('São Paulo', 'Corinthias' , 'Palmeiras', 'Santos', 'Vasco', 'Avai', 'Chapecoense', 'flamengo', 'botafogo',
                'fluminense', 'Grêmio', 'Internacional', 'Bahia', 'Ceará', 'Fortaleza', 'Curitiba', 'America mineiro',
                'Goiás', 'Bragantino', 'Guarani')
print('Os 5 primeiros colocados:')

for pos, time in enumerate(soccer_table [:5], start=1):
    print(f'{pos}º - {time}')
    print('=' * 20)

print('Os últimos 4 colocados')

for pos, time in enumerate(soccer_table [-4:], start=len(soccer_table)-3):
    print(f'{pos}º - {time}')
    print('=' * 35)

print('Times em ordem alfabética.')
print(sorted(soccer_table))

print('=' * 35)
pos_chapecoense = soccer_table.index('Chapecoense') + 1
print(f'Chapecoense está na {pos_chapecoense}ª posição.')
