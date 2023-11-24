#Implementação completa

import os

ARQUIVO_TAREFAS = "tarefas.txt"
tarefas = {}

def salvar_tarefas():
    with open(ARQUIVO_TAREFAS, "w") as arquivo:
        for id_tarefa, (descricao, concluida) in tarefas.items():
            arquivo.write(f"{id_tarefa},{descricao},{concluida}\n")

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r") as arquivo:
            for linha in arquivo:
                id_tarefa, descricao, concluida = linha.strip().split(",")
                tarefas[int(id_tarefa)] = (descricao, concluida == "True")

def listar_tarefas():
    print("Lista de Tarefas:")
    for id_tarefa, (descricao, concluida) in tarefas.items():
        status = "[x]" if concluida else "[ ]"
        print(f"{id_tarefa}. {descricao} {status}")

def registrar_tarefa():
    descricao = input("Digite a descrição da nova tarefa: ").capitalize()
    id_tarefa = len(tarefas) + 1
    tarefas[id_tarefa] = (descricao, False)
    print("Tarefa registrada!!!")

def marcar_como_realizada():
    id_tarefa = int(input("Digite o ID da tarefa a ser marcada como realizada: "))
    if id_tarefa in tarefas and not tarefas[id_tarefa][1]:
        tarefas[id_tarefa] = (tarefas[id_tarefa][0], True)
        print("Tarefa marcada como realizada!!!")
    else:
        print("Tarefa não encontrada ou já realizada.")

def editar_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa a ser editada: "))
    if id_tarefa in tarefas:
        nova_descricao = input("Digite a nova descrição da tarefa: ").capitalize()
        tarefas[id_tarefa] = (nova_descricao, tarefas[id_tarefa][1])
        print("Tarefa editada!!!")
    else:
        print("Tarefa não encontrada.")

def menu():
    print("\n===== ToDoList App =====")
    print("1. Listar Tarefas")
    print("2. Registrar Nova Tarefa")
    print("3. Marcar Tarefa como Realizada")
    print("4. Editar Tarefa")
    print("0. Sair")

def main():
    carregar_tarefas()

    while True:
        menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            listar_tarefas()
        elif opcao == "2":
            registrar_tarefa()
        elif opcao == "3":
            marcar_como_realizada()
        elif opcao == "4":
            editar_tarefa()
        elif opcao == "0":
            salvar_tarefas()
            print("Saindo do aplicativo. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

