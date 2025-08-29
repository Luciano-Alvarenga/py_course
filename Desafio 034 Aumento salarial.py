#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

#Para salários superiores a R$1.250.00, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%.

salary = float(input('Qual é o salário do funcionário? '))
if salary <= 1250.00:
    new_salary = salary + (salary * 15/100)
    print(f'Quem ganhava um salário de R$ {salary:.2f} vai passar a ganhar R${new_salary:.2f} com 15% de aumento.')

else:
    new_salary = salary + (salary * 10/100)
    print(f'Quem ganhava um salário de R${salary:.2f} vai passar a ganhar R${new_salary:.2f} com 10% de aumento.')