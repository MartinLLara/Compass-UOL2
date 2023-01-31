"""Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada.
 A classe Lampada possuí os seguintes métodos:

liga(): muda o estado da lâmpada para ligada

desliga(): muda o estado da lâmpada para desligada

esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

Para testar sua classe:
Ligue a Lampada

Imprima: A lâmpada está ligada? True

Desligue a Lampada

Imprima: A lâmpada ainda está ligada? False
"""
class Lampada:
    
    def __init__(self, voltagem, brilho):
        self.__voltagem = voltagem
        self.__brilho = brilho
        self.__ligada = False
    
    def liga(self):
        self.__ligada = True
        print(f'A lâmpada está ligada? {self.__ligada}')
    def desliga(self):
        self.ligada = False
        print(f'A lâmpada ainda está ligada? {self.ligada}')
lamp = Lampada(220,50)
lamp.liga()
lamp.desliga()    
