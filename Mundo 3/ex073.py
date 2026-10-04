# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times. b) Os últimos 4 colocados.
# c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

times = ('Flamengo', 'Palmeiras', 'Atlético-PR', 'Fluminense', 'Bahia', 'Cruzeiro', 'Atlético-MG', 'Santos', 'Coritiba',
'São Paulo', 'Red Bull Bragantino', 'Botafogo', 'Vitória', 'Corinthians', 'Mirassol', 'Vasco da Gama', 'Grêmio', 'Internacional',
'Remo', 'Chapecoense')
print('==' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('==' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('==' * 15)
print(f'Os últimos 4 times são: {times[-4:]}')
print('==' * 15)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('==' * 15)
print(f'O Chapeconse está na {times.index('Chapecoense')+1}ª posição')
