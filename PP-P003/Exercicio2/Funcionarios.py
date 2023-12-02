def cadastrarNovoFuncionario(lista_funcionarios):
    print("Informe o RG do funcionário")
    rg = input()
    if any(func["RG"] == rg for func in lista_funcionarios):
        print("Este funcionário já está cadastrado")
        return
    print("Informe o nome do funcionário")
    nome = input().capitalize()
    print("Informe o sobrenome do funcionário")
    sobrenome = input().capitalize()
    print("Informe o ano de admissão do funcionário")
    admissao = input()
    print("Informe o salário do funcionário")
    salario = float(input())
    lista_funcionarios.append({"RG": rg, "nome": nome, "sobrenome": sobrenome, "admissao": admissao, "salario": salario})


def listarTodosFuncionarios(lista_funcionarios):
    funcionarios_ordenados = sorted(lista_funcionarios, key=lambda func: func['nome'])
    for func in funcionarios_ordenados:
        print(f"RG: {func['RG']}")
        print(f"Nome: {func['nome']}")
        print(f"Sobrenome: {func['sobrenome']}")
        print(f"Ano de admissão: {func['admissao']}")
        print(f"Salário: R${func['salario']: .2f}")

def consultarFuncionarioPorRG(lista_funcionarios):
    print("Informe o RG do funcionário")
    rg = input()
    for func in lista_funcionarios:
        if func["RG"] == rg:
            print(f"Nome: {func['nome']}")
            print(f"Sobrenome: {func['sobrenome']}")
            print(f"Ano de admissão: {func['admissao']}")
            print(f"Salário: R${func['salario']: .2f}")



def carregarFuncionariosDoArquivo():
    lista_funcionarios = []
    try:
        with open("funcionarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for i in range(0, len(linhas), 5):
                rg = linhas[i].strip()
                nome = linhas[i + 1].strip()
                sobrenome = linhas[i + 2].strip()
                admissao = linhas[i + 3].strip()
                salario = float(linhas[i + 4].strip())
                lista_funcionarios.append({"RG": rg, "nome": nome, "sobrenome": sobrenome, "admissao": admissao, "salario": salario})
        return lista_funcionarios
    except Exception as erro:
        print(f"Erro ao ler funcionários: {erro}")
        return lista_funcionarios

def salvarFuncionariosNoArquivo(lista_funcionarios):
    try:
        with open("funcionarios.txt", "w") as arquivo:
            for func in lista_funcionarios:
                arquivo.write(func["RG"] + "\n")
                arquivo.write(func["nome"] + "\n")
                arquivo.write(func["sobrenome"] + "\n")
                arquivo.write(func["admissao"] + "\n")
                arquivo.write(str(func["salario"]) + "\n")
    except Exception as erro:
        print(f"Erro ao salvar funcionários: {erro}")
