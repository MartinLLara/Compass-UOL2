import requests as rq
import json as js
import pandas as pd

chaveapi='a508de41f0074e15e7b381d9ddf06a15'

url='https://api.themoviedb.org/3/collection/131295-captain-america-collection?api_key=a508de41f0074e15e7b381d9ddf06a15&language=pt-BR'

response=rq.get(url)
data=response.json()

filmes=[]

for movie in data['parts']:
    df={'Titulo': movie['title'],'Data Lançamento':movie['release_date'],'Visão geral':movie['overview'],'Votos':movie['vote_count'],'Média de Votos':movie['vote_average']}
    filmes.append(df)
df=pd.DataFrame(filmes)
print(df)
