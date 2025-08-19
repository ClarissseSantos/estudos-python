n1= int(input("digite o primeiro número:"))
n2= int(input("digite o segundo número:"))
n3= int(input("digite o terceiro número:"))
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor é o',(maior))
