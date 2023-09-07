def calcular_reajuste_salario(sal_atual):
    if sal_atual <= 280:
        percentual_aumento = 20
    elif sal_atual <= 700:
        percentual_aumento = 15
    elif sal_atual <= 1500:
        percentual_aumento = 10
    else:
        percentual_aumento = 5
    
    aumento = (sal_atual * percentual_aumento) / 100
    novo_salario = sal_atual + aumento
    
    return percentual_aumento, aumento, novo_salario

while True:

    sal_atual = float(input("Informe o salário atual do colaborador: R$ "))
    percentual, aumento, novo_sal = calcular_reajuste_salario(sal_atual)

    print("\n=== Resultados ===")
    print(f"Salário antes do reajuste: R$ {sal_atual:.2f}")
    print(f"Percentual de aumento aplicado: {percentual}%")
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Novo salário após o aumento: R$ {novo_sal:.2f}")

    continuar = input("\nDeseja calcular novamente? (S para sim, N para sair)").strip().upper()
    if continuar != 'S':
        break
