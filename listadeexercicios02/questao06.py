qnt_ganha = int(input("Quanto ganha por hora?"))
horas_trabalhadas = int(input('horas trabalhadas por mes:'))
salário_bruto = qnt_ganha * horas_trabalhadas
ir = salário_bruto * 0.11
inss = salário_bruto * 0.08
sindicato = salário_bruto * 0.05
print(f'+ Salário Bruto: R$ %.2f' %salário_bruto)
print(f'- IR: R$ %.2f' %ir)
print(f'- INSS: R$ %.2f' %inss)
print(f'-Sindicato: R$ %.2f' %sindicato)
print(f'= Salário Liquido: R$ %.2f' %(salário_bruto - ir - inss - sindicato))
