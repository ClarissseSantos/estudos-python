preçodamercadoria = int(input("digite o preço da mercadoria:"))
desconto = int(input("digite o desconto:"))
print (" o valor da compra foi R$" , (preçodamercadoria - (preçodamercadoria*desconto/100)))
print (" o valor do desconto foi R$", ((preçodamercadoria - ((preçodamercadoria*desconto/100)))-preçodamercadoria))
