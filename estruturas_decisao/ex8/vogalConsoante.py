def verificar_vogal_ou_consoante(letra):
    if letra in "aeiouAEIOU":
        return "vogal"
    elif letra.isalpha():
        return "consoante"
    else:
        return "caractere inválido"

while True:
    letra = input("Digite uma letra: ").strip().lower()
    res = verificar_vogal_ou_consoante(letra)

    print(f"A letra '{letra}' é uma {res}.")
    continuar = input("Deseja verificar outra letra? (S para sim, N para sair) ").strip().upper()
    if continuar != 'S':
        break
