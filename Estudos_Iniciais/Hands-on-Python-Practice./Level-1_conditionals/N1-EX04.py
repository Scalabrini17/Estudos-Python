# calculando IMC

print('Calculadora de IMC!')

peso = int(input('Digite o seu peso (Kg): '))
altura = int(input('Digite sua altura (m): '))

imc = peso / (altura ** 2)

print(f'Seu IMC é de: {imc}')

if imc < 18.5:
    print('Você está abaixo do peso normal!')
elif 18.5 <= imc < 25:
    print('Seu peso está normal!')
elif imc > 25:
    print('Seu peso está acima do normal!')