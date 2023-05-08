#Faça um Programa que peça a temperatura em graus Fahrenheit, 
#transforme e mostre a temperatura em graus Celsius.
# c = 5 * ((f-32) / 9).

f=input("Qual a temperatura em graus Fahrenheit? ")
x=float(f)
print(x)
c = 5 * ((x-32) / 9)
print(c)