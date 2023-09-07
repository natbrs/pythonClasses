def calcular_desconto_ir(sal_bruto):
    if sal_bruto <= 900:
        desconto_ir = 0
    elif sal_bruto <= 1500:
        desconto_ir = sal_bruto * 0.05
    elif sal_bruto <= 2500:
        desconto_ir = sal_bruto * 0.1
    else:
        desconto_ir = sal_bruto * 0.2
    return desconto_ir

while True:
    valor_hora = float(input("Informe o valor da hora de trabalho: R$ "))
    horas = float(input("Informe a quantidade de horas trabalhadas no mês: "))
    sal_bruto = valor_hora * horas

    des_ir = calcular_desconto_ir(sal_bruto)
    des_inss = sal_bruto * 0.1
    fgts = sal_bruto * 0.11
    total_des = des_ir + des_inss

    sal_liquido = sal_bruto - total_des

    print("\n=== Folha de Pagamento ===")
    print(f"Salário Bruto: R$ {sal_bruto:.2f}")
    print(f"(-) IR: R$ {des_ir:.2f}")
    print(f"(-) INSS: R$ {des_inss:.2f}")
    print(f"FGTS: R$ {fgts:.2f}")
    print(f"Total de descontos: R$ {total_des:.2f}")
    print(f"Salário Líquido: R$ {sal_liquido:.2f}")

    continuar = input("\nDeseja calcular novamente? (S para sim, N para sair)?").strip().upper()
    if continuar != 'S':
        break