"""Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e 
o resultado deverá ser a contagem de vogais presentes em seu conteúdo.



É obrigatório aplicar as seguintes funções:

len

filter

lambda



Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código."""




def conta_vogais(texto:str)-> int:
    txt=filter(lambda x: x == 'a',texto)
    print(txt)
conta_vogais('a')