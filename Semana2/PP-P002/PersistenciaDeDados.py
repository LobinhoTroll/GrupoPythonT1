import pickle
import os

class ToDoList:
    def __init__(self):
        self.tarefas = []
        self.arquivo_tarefas = 'Semana2/PP-P002/tarefas.pkl'

        if os.path.exists(self.arquivo_tarefas):
            with open(self.arquivo_tarefas, 'rb') as arquivo:
                self.tarefas = pickle.load(arquivo)

    def salvar_tarefas(self):
        # Salva as tarefas no arquivo
        with open(self.arquivo_tarefas, 'wb') as arquivo:
            pickle.dump(self.tarefas, arquivo)

    def listar_tarefas(self):
        for i, tarefa in enumerate(self.tarefas, start=1):
            print(f"{tarefa}")

    def registrar_tarefa(self, descricao):
        if descricao[0].isupper():
            nova_tarefa = f"{len(self.tarefas) + 1}. {descricao} [ ]"
            self.tarefas.append(nova_tarefa)
            self.salvar_tarefas()
            print("Tarefa registrada!!!")
        else:
            print("A descrição da tarefa deve começar com letra maiúscula.")

    def marcar_como_realizada(self, identificador):
        try:
            identificador = int(identificador)
            if 1 <= identificador <= len(self.tarefas):
                tarefa = self.tarefas.pop(identificador - 1)
                self.tarefas.insert(0, tarefa.replace("[ ]", "[x]", 1))
                self.salvar_tarefas()
                print("Tarefa marcada como realizada!!!")
            else:
                print("Identificador inválido.")
        except ValueError:
            print("Por favor, insira um identificador válido.")

    def editar_tarefa(self, identificador, nova_descricao):
        try:
            identificador = int(identificador)
            if 1 <= identificador <= len(self.tarefas):
                tarefa = self.tarefas[identificador - 1]
                status_box = tarefa[-3:-1]
                self.tarefas[identificador - 1] = f"{identificador}. {nova_descricao} {status_box}]"
                self.salvar_tarefas()
                print("Tarefa editada com sucesso!!!")
            else:
                print("Identificador inválido.")
        except ValueError:
            print("Por favor, insira um identificador válido.")

todo_list = ToDoList()

while True:

    print("\n==== ToDoList ====")
    print("1. Listar tarefas")
    print("2. Registrar nova tarefa")
    print("3. Marcar tarefa como realizada")
    print("4. Editar tarefa")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        todo_list.listar_tarefas()
    elif opcao == "2":
        descricao = input("\nDigite a descrição da nova tarefa: ")
        todo_list.registrar_tarefa(descricao)
    elif opcao == "3":
        identificador = input("\nDigite o identificador da tarefa a ser marcada como realizada: ")
        todo_list.marcar_como_realizada(identificador)
    elif opcao == "4":
        identificador = input("\nDigite o identificador da tarefa a ser editada: ")
        nova_descricao = input("Digite a nova descrição da tarefa: ")
        todo_list.editar_tarefa(identificador, nova_descricao)
    elif opcao == "0":
        print("\nSaindo do ToDoList. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")