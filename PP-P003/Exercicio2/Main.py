from Funcionarios import (cadastrarNovoFuncionario, excluirFuncionario, listarTodosFuncionarios,
                                consultarFuncionarioPorRG,
                                carregarFuncionariosDoArquivo, salvarFuncionariosNoArquivo)

def main():
    funcionarios = carregarFuncionariosDoArquivo()

    while True:
        print("\n=== Menu ===")
        print("1. Cadastrar Novo Funcionário")
        print("2. Excluir Funcionário")
        print("3. Listar Todos os Funcionários")
        print("4. Consultar Funcionário por RG")
        print("5. Reajustar Salários em 10%")
        print("6. Sair")

        opcao = input("Escolha uma opção (1-6): ")

        if opcao == "1":
            cadastrarNovoFuncionario(funcionarios)
        elif opcao == "2":
            excluirFuncionario(funcionarios)
        elif opcao == "3":
            listarTodosFuncionarios(funcionarios)
        elif opcao == "4":
            consultarFuncionarioPorRG(funcionarios)
        elif opcao == "5":
            break
        elif opcao == "6":
            salvarFuncionariosNoArquivo(funcionarios)
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
