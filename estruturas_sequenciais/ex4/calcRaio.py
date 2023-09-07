while True:
    import math 

    def calcular_area_circulo(raio):
       return math.pi * raio ** 2

    raio = float(input("Informe o raio do círculo: "))
    area = calcular_area_circulo(raio)

    print("\n=== Cálculo da Área de um Círculo ===")

    print(f"Raio do círculo: {raio:.2f} unidades")
    print(f"Área do círculo: {area:.2f} unidades quadradas")

    print("\nObrigado por utilizar nosso programa!")

    continuar = input("Quer calcular novamente? (S para sim, N para sair)? ").strip().upper()
    if continuar != 'S':
        break 
