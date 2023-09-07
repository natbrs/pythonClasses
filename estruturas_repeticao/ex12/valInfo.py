def val_nome(nome):
    return len(nome) > 3

def val_idade(idade):
    return 0 <= idade <= 150

def val_salario(salario):
    return salario > 0

def val_sexo(sexo):
    return sexo in ('f', 'm', 'nb')

def val_civil(estado_civil):
    return estado_civil in ('s', 'c', 'v', 'd')

while True:
    nome = input("Informe o nome (maior que 3 caracteres): ").strip()
    idade = int(input("Informe a idade (entre 0 e 150): "))
    salario = float(input("Informe o salário (maior que zero): "))
    sexo = input("Informe o sexo (f para feminino | m para masculino | nb para não-binário): ").strip().lower()
    estado_civil = input("Informe o estado civil (s para solteiro, c para casado, v para viúvo, d para divorciado): ").strip().lower()

    if (
        val_nome(nome) and
        val_idade(idade) and
        val_salario(salario) and
        val_sexo(sexo) and
        val_civil(estado_civil)
    ):
        print("\n=== Informações Válidas ===")
        print(f"Nome: {nome}")
        print(f"Idade: {idade} anos")
        print(f"Salário: R$ {salario:.2f}")
        print(f"Sexo: {sexo}")
        print(f"Estado Civil: {estado_civil}")
    else:
        print("\n=== Informações Inválidas ===")
        print("Por favor, verifique as informações fornecidas.")

    continuar = input("\nDeseja inserir outras informações? (S para sim, N para sair)").strip().upper()
    if continuar != 'S':
        break
