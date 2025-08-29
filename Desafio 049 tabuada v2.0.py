#Refaça o disafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.


number = int(input('Digite um valor: '))

for multiplication_table in range(1, 11):

    print(f'{number} x {multiplication_table} = {number * multiplication_table}')
