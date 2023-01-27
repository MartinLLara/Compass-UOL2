#Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.



a=['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def semrep(list):
    lista=[]
    for i in list:
        if i not in lista:
            lista.append(i)
    lista.sort()
    print(lista)

semrep(a)