def conv_centimetros(metros):
    return metros * 100

while True:

    metros = float(input("Informe a quantidade de metros que deseja converter para centímetros: "))
    cent = conv_centimetros(metros)

    print("\n=== Conversão de Metros para Centímetros ===")
    print(f"{metros} metros equivalem a {cent} centímetros.")

    continuar = input("\nDeseja continuar (S para sim, N para sair)? ").strip().upper()
    if continuar != 'S':
        break
