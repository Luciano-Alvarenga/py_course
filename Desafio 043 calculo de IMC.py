#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre o seu status, de acordo
#com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso.
# - Entre 18.5 e 25: Peso ideal.
# - 25 até 30: Sobrepeso.
# - Acima de 40: Obesidade mórbida.

weight = float(input('Digite o seu peso: '))
height = float(input('Digite a sua altura: '))
IMC = weight / height ** 2
print(f'Seu imc é de {IMC:.2f}')

if IMC < 18.5:
    print('Você está ABAIXO do PESO!')
if 18.5 <= IMC <= 25:
     print('Você está no PESO IDEAL!')
elif 25<= IMC <= 30:
     print('Você está com SOBREPESO!')
else:
      print('Você está com OBESIDADE MÓRBIDA!')
      