#Dada a seguinte lista:



a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



#Faça um programa que gere uma nova lista contendo apenas números ímpares.
b=[]
for i in a:
    if i%2 == 1:
        b.append(i)
print(b)