while True:
    nome = input("Informe o seu nome: ")

    val_hora = float(input("Informe o valor que você ganha por hora: "))
    horas = float(input("Informe o número de horas trabalhadas no mês: "))

    sal_mensal = val_hora * horas

    print("\n=== Resumo do Salário de", nome, "===")

    print(f"Salário base: R$ {val_hora:.2f} por hora")
    print(f"Horas trabalhadas no mês: {horas:.2f} horas")
    print(f"Salário Mensal: R$ {sal_mensal:.2f}")

    continuar = input("Quer calcular novamente? (S para sim, N para sair)? ").strip().upper()
    if continuar != 'S':
        break 