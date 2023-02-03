import re

with open ("actors.csv",'r') as actors:
     reg= actors.readlines()
     listaactor = []
     for i in range(0,len(reg)):
          dadostr= reg[i]
          dadostr = re.sub(r", Jr", " Jr", dadostr)
          dado = dadostr.split(',')
          listaactor.append(dado)
filmes = {}
for i in range(1,len(listaactor)):
    aux = listaactor[i][4]
    if aux not in filmes:
        filmes[listaactor [i][4]]=1
    else:
        filmes[listaactor [i][4]]+=1
filmes_ord = {k: v for k, v in sorted(filmes.items(), key=lambda item: item[1], reverse=True)}
texto = 'O filme mais frequente e sua frequencia:' + '\n'
texto += str(filmes_ord)
print(texto)

with open ('arquivo4.txt','w') as filmesfrequencia:
    filmesfrequencia.write(texto)