import re

with open ("actors.csv",'r') as actors:
     reg= actors.readlines()
     listaactor = []
     for i in range(0,len(reg)):
          dadostr= reg[i]
          dadostr = re.sub(r", Jr", " Jr", dadostr)
          dado = dadostr.split(',')
          listaactor.append(dado)
atores = {}
for i in range(1,len(listaactor)):
    atores[listaactor[i][0]]= listaactor[i][5]
atores_ord = {k: v for k, v in sorted(atores.items(), key=lambda item: item[1], reverse=True)}
texto = 'Lista de atores ordenada por pagamento, do maior ao menor' +'\n'
texto += str(atores)
print(texto)
with open ('arquivo5.txt','w') as listapagamento:
    listapagamento.write(texto)