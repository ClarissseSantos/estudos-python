tamanho = int(input("Tamanho em metros quadrados:"))
litro = tamanho / 3
if tamanho %54 == 0:
    latas = tamanho / 54
else:
    latas = int(tamanho / 54)+1
preço = latas*80
print(f' terá que comprar %d latas'%latas)
print(f' custará R$ %.2f' %preço)
