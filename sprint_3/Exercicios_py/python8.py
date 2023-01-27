"""Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.

Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente."""
palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
for i in palavras:
    if i == i[::-1]:
        print(f'{i} é um palíndromo')
    else:
        print(f'{i} não é um palíndromo')