#Escreva um programa que leia um valor em metros e o exiba convertido em kilométros km, hectômetros hm, decâmetros dam, decímetro dm, centímetros cm e milímitros mm.
medida = float(input('Digite uma distâcia em metros: '))
km = medida * 0.01
hm = medida * 0.1
dam = medida * 1
dm = medida * 10
cm = medida * 100
mm = medida *1000
print (f'O valor de {medida}m Corresponde a: \n{km} kilométros \n{hm} hectômetros \n{dam} decâmetros \n{dm} decímetros \n{cm} centímetros \n{mm} milímetros')