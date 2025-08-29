#Refaça o desafio 035 dos triângulos, acresentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados são iguais.
# - Isósceles: dois lados iguais.
# - Escaleno: todos os lados diferentes.

print('Informe o comprimento das 3 retas!')

straight_1 = float(input('Digire a primeira reta: '))
straight_2 = float(input('Digite a segunda reta: '))
straight_3 = float(input('Digite a terceira reta: '))

if straight_1 + straight_2 > straight_3 and straight_1 + straight_3 > straight_2 and straight_2 + straight_3 > straight_1:
    print('As retas podem forma um triângulo ')
    if straight_1 == straight_2 == straight_3:
        print('O triângulo é EQUILÁTERO: Todos os lados são iguais!')
    elif straight_1 == straight_2 or straight_1 == straight_3 or straight_2 == straight_3:
        print('O triângulo é ISÓSCELES: Dois lados são iguais!')
    else:
        print('O triângulo é ESCALENO: todos os lados são diferentes!')

else:print('As retas não podem forma um triângulo!')