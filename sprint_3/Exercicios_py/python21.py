"""Implemente duas classes Pato e Pardal que herdem de uma classe Passaro a habilidade de voar e emitir som, porém, 
tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console.



Imprima no console exatamente assim:

Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu"""
"""
class Passaro:

 
    def _init_(self,nome):
        self.__nome=nome
        
    def voar(self):
            print(f'({self.__nome}\nVoando...')
    def canto_pato(self):
        print('Quack Quack')
    def canto_pardal(self):
        print('Piu Piu')
    def som(self):
        print(f'{self.__nome} emitindo som...')
    
class Pato(Passaro):
    def _init_(sel,nome):
        super().__init__(nome)
class Pardal(Passaro):
    def __init__(self,nome): 
         super().__init__(nome)
    
pato=Pato('Pato')
pardal = Pardal('Pardal')
pato.voar
pato.canto_pato
pardal.voar
pardal.canto_pardal
"""
class Passaro:
   def _init_(self, nome):
       self.nome = nome


   def voar(self):
       print(f'{self.nome} \nVoando...')


   def emitir_som(self):
       print(f'{self.nome} emitindo som...')


   def pato_som(self):
       print('Quack Quack')


   def pardal_som(self):
       print('Piu Piu')


class Pato(Passaro):
   def _init_(self, nome):
       super()._init_(nome)


class Pardal(Passaro):
   def _init_(self, nome):
      super()._init_(nome)


pato = Pato(0)
pardal = Pardal('Pardal')


pato.voar()
pato.emitir_som()
pato.pato_som()
pardal.voar()
pardal.emitir_som()
pardal.pardal_som()