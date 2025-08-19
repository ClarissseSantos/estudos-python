n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

while n2 != 0:
	n1, n2 = n2, n1 % n2
	
print ("MDC =", n1)


