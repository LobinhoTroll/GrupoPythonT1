
def loadTasksFromFile():
    task_id = 0
    task_list = []
    try:
        tasks_file = open("tasks.txt", "r")
        for task in tasks_file:
            task_list.append(task.split("\n")[0])
            task_id += 1
        tasks_file.close()
        return task_id, task_list
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado. Criando novo arquivo 'tasks.txt'.")
        with open("tasks.txt", "w"):
            pass
        return task_id, task_list
    except Exception as e:
        print(f"Erro ao carregar as tarefas: {e}")
        return task_id, task_list

def main():
    task_id ,task_list = loadTasksFromFile()
    while True:
        print("////////// MENU //////////")
        print("1- Adcionar Tarefa")
        print("2- Marcar como Realizada")
        print("3- Editar Tarefa")
        print("4- Listar As Tarefas")
        print("0- Sair do programa")
        op = int(input())

        match op:
            case 1:
                print("Informe a descrição da tarefa:")
                description = input()
                task = str(task_id) + ".\t" + description.capitalize() + "[ ]"
                task_list.append(task)
                task_id += 1
            case 2:
                break
            case 3:
                break
            case 4:
               break
            case 5:
                break
            case _:
                print("Opção inválida")
                
if __name__ == "__main__":
    main()