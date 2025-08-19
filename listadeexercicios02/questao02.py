ano = str(input("digite um ano:"))
if int(ano)% 4 == 0 and ano[2:]!="00":
    print("é um ano bissexto")
else:
    print ("não é um ano bissexto")
