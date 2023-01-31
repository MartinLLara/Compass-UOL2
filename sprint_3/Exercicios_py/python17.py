"""Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo



lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"""

#def div_lista(list,n):
#    list2 = []
#    for i in range(0,len(list),n):
#        list2.append(i)
#    print(list2)

#lista1=[1,2,3,4,5,6,7,8,9,10,11,12]
#div_lista(lista1,3)

def divlista(lst, n):
    
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        

lista = [1,2,3,4,5,6,7,8,9,10,11,12]
lista2= list(divlista(lista,3))
print(lista2)
