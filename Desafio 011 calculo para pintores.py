#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a siua área e a quantidade de tinta necessária para pinta-lo, sabendo qiue cada litro de tinta pinta uma área de 2m².
height = float(input('Digite a altura: '))
width = float(input('Digite a largura: '))
area = height * width
print (f'A sua parede tem dimensões de {height} x {width} e a sua área e de {area}m²')
paint = area / 2
print (f'Para pintar a parede, você precisará de {paint}L de tinta.')