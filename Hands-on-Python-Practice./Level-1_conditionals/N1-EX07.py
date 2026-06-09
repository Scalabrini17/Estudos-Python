

print('Sistema para verificação da média do aluno')

soma_nota = 0

for i in range(1,4):
 nota = float(input(f'Digite a {i}º nota do aluno: '))
 soma_nota += nota

média_aluno = soma_nota / i 

print(F'A média do aluno é: {média_aluno:.2f}')