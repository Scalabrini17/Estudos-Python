#Calculando o tempo total de projeto

nome_atividade1 = input('Digite o nome da primeira atividade: ')
nome_atividade2 = input('Digite o nome da segunda atividade: ')
nome_atividade3 = input('Digite o nome da terceira atividade: ')

num_dias1 = int(input(f'Digite o número de dias da {nome_atividade1}: '))
num_dias2 = int(input(f'Digite o número de dias da {nome_atividade2}: '))
num_dias3 = int(input(f'Digite o número de dias da {nome_atividade3}: '))

mensagem_final = ''

if num_dias1 >= 0 and num_dias2 >= 0 and num_dias3 >= 0:
    tempo_total = num_dias1 + num_dias2 + num_dias3
    mensagem_final = f'O tempo total do projeto é de {tempo_total}'
    
else:
    mensagem_final = 'Erro: Os dias não podem ser negativos!'


print(f'Os dias para a atividade {nome_atividade1}: {num_dias1} \n'
      f'Os dias para a atividade {nome_atividade2}: {num_dias2} \n'
      f'Os dias para a atividade {nome_atividade3}: {num_dias3} \n'
      f'{mensagem_final}')