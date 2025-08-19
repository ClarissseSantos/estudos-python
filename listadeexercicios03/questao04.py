fibo = [1,1]
i = 0
número = int(input("Digite um número: "))

while número > len(fibo):
	fibo.append(fibo[i] + fibo[i+1])
	i +=1

print ('Fibonacci(%d): %d' %(número,fibo[número-1]))
