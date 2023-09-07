val_hora = float(input("Informe o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))

sal_bruto = val_hora * horas_trabalhadas
imp_renda = sal_bruto * 0.11
inss = sal_bruto * 0.08
sindicato = sal_bruto * 0.05

sal_liquido = sal_bruto - imp_renda - inss - sindicato

print("+ Salário Bruto : R$ {:.2f}".format(sal_bruto))
print("- IR (11%) : R$ {:.2f}".format(imp_renda))
print("- INSS (8%) : R$ {:.2f}".format(inss))
print("- Sindicato (5%) : R$ {:.2f}".format(sindicato))
print("= Salário Líquido : R$ {:.2f}".format(sal_liquido))]