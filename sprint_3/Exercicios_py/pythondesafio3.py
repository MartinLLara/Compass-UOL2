import re

with open ("actors.csv",'r') as actors:
     reg= actors.readlines()
     listaactor = []
     for i in range(0,len(reg)):
          dadostr= reg[i]
          dadostr = re.sub(r", Jr", " Jr", dadostr)
          dado = dadostr.split(',')
          listaactor.append(dado)
atormaiormedia = ''
mediapfilme=0
for i in range(1,len(listaactor)):
    if float(listaactor[i][3]) >= mediapfilme:
        mediapfilme= float(listaactor[i][3])
        atormaiormedia = listaactor[i][0]
texto = 'O ator com maior media de filme :' + '\n'
texto += str(atormaiormedia) + '\n'
texto += str(mediapfilme)
print(texto)
with open ('arquivo3.txt','w') as mediafilme:
    mediafilme.write(texto)