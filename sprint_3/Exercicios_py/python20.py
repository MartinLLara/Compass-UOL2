"""Imprima a lista abaixo de trás para frente.

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]"""

a= [1,0,2,3,5,8,13,21,34,55,89]
b=[]
for i in reversed(a):
    b.append(i)
print(b)