def calcular_situacao_aluno(media):
    if media == 10:
        return "Aprovado com Distinção"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

while True:
    n1 = float(input("Informe a primeira nota: "))
    n2 = float(input("Informe a segunda nota: "))

    media = (n1 + n2) / 2

    print(f"A média do aluno é: {media:.2f}")
    situacao = calcular_situacao_aluno(media)

    print(f"Situação do aluno: {situacao}")
    continuar = input("Deseja calcular a média novamente? (S para sim, N para sair)").strip().upper()
    if continuar != 'S':
        break