"""Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. 
Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).



Utilize os valores abaixo para testar seu exercício:

x = 4 
y = 5
imprima:

Somando: 4+5 = 9
Subtraindo: 4-5 = -1"""

class Calculo:
    def __init__(self,X,Y):
        self.__X = X
        self.__Y = Y
    def sub(self):
        z = self.__X - self.__Y
        print(f'Subtraindo: {self.__X}+{self.__Y} = {z}')
    def som(self):
        u = self.__X + self.__Y
        print(f'Somando: {self.__X}+{self.__Y} = {u}')

cal=Calculo(4,5)
cal.som()
cal.sub()