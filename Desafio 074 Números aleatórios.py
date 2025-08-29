# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numbers = tuple(randint(0, 100) for _ in range(5))

print(f'Números sorteados {numbers}')

print(f'O número maior foi {max(numbers)}')
print(f'O menor número foi {min(numbers)}')