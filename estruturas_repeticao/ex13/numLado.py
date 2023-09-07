while True:
    print("Imprimindo os números de 1 a 20 um abaixo do outro:")
    for numero in range(1, 21):
        print(numero)
    
    continuar = input("\nQuer imprimir novamente? (S para sim, N para sair)").strip().upper()
    if continuar != 'S':
        break