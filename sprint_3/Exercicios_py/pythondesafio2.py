import re

with open ("actors.csv",'r') as actors:
     reg= actors.readlines()
     listaactor = []
     for i in range(0,len(reg)):
          dadostr= reg[i]
          dadostr = re.sub(r", Jr", " Jr", dadostr)
          dado = dadostr.split(',')
          listaactor.append(dado)

totalfilmes = 0
for i in range(1,len(listaactor)):
    totalfilmes += int(listaactor[i][2])
mediafilmes = totalfilmes/int(len(listaactor))
texto = "A media de filmes por ator é" + '\n'
texto += str(mediafilmes)
print (texto)
with open('arquivo2.txt','w') as media:
    media.write(texto)
