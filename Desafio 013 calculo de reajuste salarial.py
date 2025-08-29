#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
salary = float(input('Qual é o salário do Funcionário? '))
new = salary + (salary * 15/100)
print (f'O salário funcionário de R${salary:.2f}, com um aunmento de 15% de aumento vai para R${new:.2f}')