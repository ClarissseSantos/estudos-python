l1 = int(input("Lado 1: "))
l2 = int(input("Lado 2: "))
l3 = int(input("Lado 3: "))
if l1 >(l2+l3) or 12 > (11+13) or 13 >(11+12):
     print ("Não pode ser um triangulo")
elif l1 == l2 == l3:
     print ("é um equilátero")
elif l1 == l2 or l1 == l3 or 12 == 13:
     print ("é um isósceles")
else:
    print ("é um escaleno")
  
