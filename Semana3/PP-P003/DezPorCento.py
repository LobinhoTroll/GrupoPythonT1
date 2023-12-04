import os

empregados = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def reajusta_dez_porcento(lista_empregados):
    for empregado in lista_empregados:
        empregado['salario'] *= 1.1  

def carregar_dados_arquivo():
    try:
        with open('/home/felipe/Área de Trabalho/Residencia/GrupoPythonT1/Semana3/PP-P003/funcionarios.txt', 'r') as file:
            for line in file:
                dados = line.strip().split()
                empregado = {
                    'nome': dados[0],
                    'sobrenome': dados[1],
                    'ano_nascimento': int(dados[2]),
                    'rg': dados[3],
                    'ano_admissao': int(dados[4]),
                    'salario': float(dados[5])
                }
                empregados.append(empregado)
        print("Dados carregados com sucesso.")
    except FileNotFoundError:
        print("Arquivo 'funcionarios.txt' não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

def exibir_empregados():
    clear_screen()
    if not empregados:
        print("Nenhum empregado cadastrado.")
    else:
        print("Lista de empregados:")
        for empregado in empregados:
            print(f"Nome: {empregado['nome']} {empregado['sobrenome']} | "
                  f"Ano de Nascimento: {empregado['ano_nascimento']} | "
                  f"RG: {empregado['rg']} | "
                  f"Ano de Admissão: {empregado['ano_admissao']} | "
                  f"Salário: R${empregado['salario']:.2f}")
    input("Pressione Enter para continuar...")

def menu():
    while True:
        clear_screen()
        print("===== Empresa =====")
        print("1. Carregar dados dos empregados")
        print("2. Exibir empregados")
        print("3. Reajustar salários em 10%")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            carregar_dados_arquivo()
        elif escolha == "2":
            exibir_empregados()
        elif escolha == "3":
            reajusta_dez_porcento(empregados)
            print("Salários reajustados em 10%.")
            input("Pressione Enter para continuar...")
        elif escolha == "0":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
