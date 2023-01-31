"""Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.



A string deve ter valor  "1,3,4,6,10,76" """

def soma(string):
    novastring = string.split(",")
    linha =[]
    for i in novastring:
        j = int(i)
        linha.append(j)
    print(sum(linha))    
    

soma('1,3,4,6,10,76')
