from functools import reduce

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

lanc2= lambda x, y: if y == 'D' x*-1
lanc3 = reduce(lanc2,lancamentos)
print (lanc3)
print (lancamentos)