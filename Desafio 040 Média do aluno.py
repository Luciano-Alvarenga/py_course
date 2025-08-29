#Crie um programa que leia as duas notas de um aluno e calcule a média, mostrando uma mensagem no final, de acordo com
#a média atingida:
# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado

note_1 = float(input('Digite a primeira nota do aluno: '))
note_2 = float(input('Digite a segunda nota do aluno: '))
average = (note_1 + note_2) / 2

if average <= 5.0:
    print('Você foi Reprovado! Tente na próxima!')

elif 5.0 <= average <= 6.9:
    print('Você está de Recuperação!')

elif average > 7.0:
    print('Você foi Aprovado! Parabéns!!!')

print(f'A sua média foi: {average}!')
