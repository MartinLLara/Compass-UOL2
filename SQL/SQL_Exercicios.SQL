E1-
select *

from livro
where publicacao >= '2015-01-01'
order by cod

E2-
select titulo, valor
from livro
order by valor desc
limit 10

E3-
SELECT COUNT(livro.editora) as quantidade, nome, estado, cidade
FROM editora
INNER JOIN livro on codeditora = editora
INNER JOIN endereco on codendereco = endereco
group by nome, estado, cidade
ORDER BY  quantidade DESC
LIMIT 5

E4-
select count(autor) as quantidade, nome, codautor, nascimento 
from autor
left join livro on autor = codautor
group by nome,codautor,nascimento
order by nome 

E5-
SELECT autor.nome
FROM autor
LEFT JOIN livro l on autor.codautor = l.autor
INNER JOIN editora e on e.codeditora = l.editora
INNER JOIN endereco e2 on e2.codendereco = e.endereco
WHERE  e2.estado <> 'RIO GRANDE DO SUL' AND e2.estado <> 'PARANÁ'
ORDER BY autor.nome ASC

E6-
select A.codautor, A.nome, count(L.autor) as quantidade_publicacoes
from livro as L
Left join autor as A on codautor = autor
group by A.codautor, A.nome
Order by quantidade_publicacoes desc
limit 1 

E7-

select nome
from autor as A
left join livro as L on autor = codautor 
where L.cod IS NULL

E8-

select TBV.cdvdd, TBVE.nmvdd
from tbvendas as TBV
left join tbvendedor as TBVE on TBVE.cdvdd = TBV.cdvdd
where TBV.status = 'Concluído'
group by TBV.cdvdd, TBVE.nmvdd
order by count(TBV.cdvdd) DESC
limit 1

E9-

select cdpro, nmpro
from tbvendas as T1
where status = 'Concluído' 
and dtven BETWEEN '2014-02-03' and '2018-02-02'
group by nmpro, cdpro
order by count (*) ASC
limit 1

E10-

Select T2.nmvdd as vendedor,
       SUM(T1.qtd * T1.vrunt) as valor_total_vendas,
       ROUND((SUM(T1.qtd * T1.vrunt * perccomissao))/100,2) as comissao
from tbvendas as T1
    left join tbvendedor as T2 on T1.cdvdd = T2.cdvdd
Where status = 'Concluído'
group by T2.nmvdd
order by comissao DESC

E11-

select cdcli, nmcli,SUM(T1.qtd * T1.vrunt) as gasto
from tbvendas as T1
where T1.status = 'Concluído'
group by cdcli, nmcli
order by gasto desc
limit 1

E12-

select cddep, nmdep, dtnasc,SUM(T1.qtd * T1.vrunt) as valor_total_vendas
from tbvendas as T1
left join tbdependente as T3 on T3.cdvdd = T1.cdvdd
where status = 'Concluído' 
group by cddep, nmdep, dtnasc
order by valor_total_vendas ASC
limit 1

E13-

select T1.cdpro, nmcanalvendas, nmpro,Sum(T1.qtd) as quantidade_vendas
from tbvendas as T1
left Join tbestoqueproduto as T4 on T4.cdpro = T1.cdpro
where T1.status = 'Concluído'
group by T1.cdpro, nmcanalvendas, nmpro
order by quantidade_vendas
limit 10

E14-

select estado,Round(avg(qtd * vrunt),2) as gastomedio
from tbvendas
where status = 'Concluído'
group by estado

E15-

select cdven
from tbvendas
where deletado = 1 
order by cdven asc

E16-

select estado, nmpro,round(AVG(qtd),4) as quantidade_media
from tbvendas
where status = 'Concluído'
group by estado, nmpro
order by estado, nmpro

