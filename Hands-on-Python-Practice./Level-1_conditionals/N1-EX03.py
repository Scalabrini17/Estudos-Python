# Temperatura dos servidores

temperatura_sala = int(input('Digite a temperatura atual da Sala de Servidores: '))

mensagem_alerta = ''

if temperatura_sala > 25: 
    mensagem_alerta = f'ALERTA DE SEGURANÇA. A temperatura da Sala de Servidores está em {temperatura_sala}ºC está passando de 25ºC!'
else: 
    mensagem_alerta = f'A temperatuda da Sala de Servidores está em {temperatura_sala}ºC, está em ótimo estado, fique tranquilo!'

print(mensagem_alerta)