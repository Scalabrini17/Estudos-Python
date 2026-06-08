# Controlando o orçamento mensal

import time

print('Bem vindo ao controle de gastos mensais')

start = input('Para iniciar e colocar os seus gastos digite (S)')

soma = 0

print('AVISO! Se quiser sair do programa em algum momento digite 0 (zero)!')
while start.upper() == 'S':
    valor = int(input('Digite o gasto: '))
    soma += valor
    if valor == 0:
        print('Finalizando o programa')
        print('Calculando...')
        time.sleep(3)
        break

if soma < 1000:
    print(f'Que boa nóticia, seus gastos estão baixos. Seus gastos até o momento é de R$ {soma}')
elif soma > 1001 and soma <= 2499:
    print(f'Seus gastos estão quase na metade, fique atento! Gasto atual: R$ {soma}')
elif soma >= 2500 and soma <= 2999:
    print(f'Sua conta setá chegando ao seu limite de R$3000. ATENÇÃO! seus gastos atuais estão em: R$ {soma}')
elif soma >=3000:
    print(f'Sua conta bateu o limite de R$3000. Alerta! Sua conta atual está em R$ {soma}')