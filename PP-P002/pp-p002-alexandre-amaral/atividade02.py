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

def saveTasksToFile(task_list):
    try:
        with open("tasks.txt", "w") as tasks_file:
            for task in task_list:
                tasks_file.write(f"{task}\n")
        print("Tarefas salvas com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar as tarefas: {e}")

def taskExists(task_list, identifier):
    for task in task_list:
        task_id = task.split(".")[0]
        status = task.find("[ ]")
        if task_id == identifier and status != -1:
            return True
    return False


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
                print("Informe o ID da tarefa:")
                identifier = int(input())
                try:
                    task_list[identifier] = task_list[identifier].replace("[ ]", "[X]")
                    print("Tarefa realizada com sucesso!")
                except:
                    continue
            case 3:
                break
            case 4:
               break
            case 5:
                saveTasksToFile(task_list)
                break
            case _:
                print("Opção inválida")
                
if __name__ == "__main__":
    main()