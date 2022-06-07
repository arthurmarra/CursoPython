# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre: A)Apenas os 5 primeiros colocados B)Os últimos 4 colocados da tabela. C)Uma lista com os times em ordem
# alfabética. D)Em que posição na tablea está o time da Chapecoense.

tabela = ('Atlético-MG','Palmeiras','Fortaleza','Bragantino','Flamengo','Corinthians','Atlético-GO','Ceará','Athletico-PR'
          ,'Internacional','Santos','São Paulo','Juventude','Cuiabá','Bahia','Fluminense','Grêmio','Sport','América-MG'
          ,'Chapecoense')
result = tabela.index('Chapecoense') +1
print(f'Lista de times do Brasileirão: {tabela}')
print('-='*15)
print(f'5 primeiros colocados: {tabela[:5]}')
print('-='*15)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-='*15)
print('A Chapecoense está na {}º posição da tabela'.format(result))
