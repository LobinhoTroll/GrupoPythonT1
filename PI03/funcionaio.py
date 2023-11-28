def Reajusta_dez_porcento(empregados):
    for empregado in empregados:
        empregado["salario"] *= 1.1


def ler_arquivo(nome_arquivo):
    empregados = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                empregado = {
                    "nome": dados[0],
                    "sobrenome": dados[1],
                    "ano_nascimento": int(dados[2]),
                    "RG": dados[3],
                    "ano_admissao": int(dados[4]),
                    "salario": float(dados[5])
                }
                empregados.append(empregado)
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
    return empregados


def escrever_arquivo(nome_arquivo, empregados):
    with open(nome_arquivo, 'w') as arquivo:
        for empregado in empregados:
            linha = f"{empregado['nome']},{empregado['sobrenome']},{empregado['ano_nascimento']},{empregado['RG']},{empregado['ano_admissao']},{empregado['salario']:.2f}\n"
            arquivo.write(linha)


def menu():
    nome_arquivo = "funcionarios.txt"
    empregados = ler_arquivo(nome_arquivo)

    while True:
        print("Menu de Opções:")
        print("1. Reajustar salários em 10%")
        print("2. Mostrar informações dos funcionários")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")
        if opcao == '1':
            Reajusta_dez_porcento(empregados)
            print("Salários reajustados em 10%.\n")
        elif opcao == '2':
            for empregado in empregados:
                print(f"Nome: {empregado['nome']} {empregado['sobrenome']}, Salário: R${empregado['salario']:.2f}")
            print()
        elif opcao == '0':
            escrever_arquivo(nome_arquivo, empregados)
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menu()
