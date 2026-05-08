

print('Sistema de calculo do pedágio')

dis = int(input('Digite o valor correspondente a distancia percorrida:' ))

pag = 0

if dis <= 100:
    pag = 10
elif dis > 100 and dis <= 200:
    pag = 20
elif dis > 200:
    pag = 30

print(f'A distancia percorrida é de {dis} Km e o valor do pedágio será de R$ {pag}')