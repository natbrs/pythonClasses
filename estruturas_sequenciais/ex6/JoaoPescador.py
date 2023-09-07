while True:
    peso_peixes = float(input("Informe o peso dos peixes em quilos: "))
    limite_peso = 50.0

    if peso_peixes > limite_peso:
      
        excesso = peso_peixes - limite_peso
        multa = excesso * 4.00

        print("Peso excedente de {:.2f} quilos.".format(excesso))
        print("Multa a pagar: R$ {:.2f}".format(multa))
    else:
        print("Peso dentro do limite estabelecido, não há multa a pagar.")

    continuar = input("Quieres continuar? (S para sim, N para sair)? ").strip().upper()
    if continuar != 'S':
        break 
