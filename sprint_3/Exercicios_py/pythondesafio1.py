import re

with open ("actors.csv",'r') as actors:
     reg= actors.readlines()
     listaactor = []
     for i in range(0,len(reg)):
          dadostr= reg[i]
          dadostr = re.sub(r", Jr", " Jr", dadostr)
          dado = dadostr.split(',')
          listaactor.append(dado)
maxfilmes= 0
atormax=''
for i in range(1,len(listaactor)):
     if int(listaactor[i][2]) >= maxfilmes:
          maxfilmes= int(listaactor[i][2])
          atormax= listaactor[i][0]
texto = "Ator com mais filmes e número respectivo de filmes." + '\n'
texto += atormax + '\n'
texto += str(maxfilmes)
print (texto)


with open('arquivo1.txt','w') as arquivoresposta:
     arquivoresposta.write(texto)
