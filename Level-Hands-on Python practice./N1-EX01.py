# Monitorando vendas no comércio

produto_nome1 = input('Qual o nome do primeiro produto?: ')
produto_nome2 = input('Qual o nome do segundo produto?: ')

produto_quantidade1 = int(input(f'Digite qual a quantidade de {produto_nome1} vendidas: '))
produto_quantidade2 = int(input(f'Digite qual a quantidade de {produto_nome2} vendidas: '))

produto_mais_vendido = ''
quantidade_mais_vendida = ''

if produto_quantidade1 > produto_quantidade2:
    produto_mais_vendido = produto_nome1
    quantidade_mais_vendida = produto_quantidade1
elif produto_quantidade2 > produto_quantidade1:
    produto_mais_vendido = produto_nome2
    quantidade_mais_vendida = produto_quantidade2

print(f'Foram vendidas {produto_quantidade1} {produto_nome1}! \n'
      f'Foram vendidas {produto_quantidade2} {produto_nome2}! \n'
      f'E o produto mais vendido foi {produto_mais_vendido} com {quantidade_mais_vendida} unidades vendidas ')