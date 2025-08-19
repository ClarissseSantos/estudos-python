peso = int(input("digite com o peso:"))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = "Zero"
    multa = "Zero"
print ('O excesso de peso foi de',str(excesso),'kg,portanto,multa é de R$', str(multa))
