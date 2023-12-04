import os

produtos = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_codigo(codigo):
    return codigo.isdigit() and len(codigo) == 13

def validar_nome(nome):
    return nome and nome[0].isupper()

def validar_preco(preco):
    try:
        float(preco)
        return True
    except ValueError:
        return False

def inserir_produto():
    clear_screen()
    codigo = input("Digite o código do produto (13 caracteres numéricos): ")
    while not validar_codigo(codigo):
        print("Código inválido. Deve conter 13 caracteres numéricos. Tente novamente.")
        codigo = input("Digite o código do produto (13 caracteres numéricos): ")

    nome = input("Digite o nome do produto: ")
    while not validar_nome(nome):
        print("Nome inválido. Deve começar com uma letra maiúscula. Tente novamente.")
        nome = input("Digite o nome do produto: ")

    preco = input("Digite o preço do produto (ex. 10.99): ")
    while not validar_preco(preco):
        print("Preço inválido. Tente novamente.")
        preco = input("Digite o preço do produto (ex. 10.99): ")

    produto = {"codigo": codigo, "nome": nome, "preco": float(preco)}
    produtos.append(produto)
    print("Produto inserido com sucesso!")

def excluir_produto():
    clear_screen()
    codigo = input("Digite o código do produto a ser excluído: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado.")

def listar_produtos():
    clear_screen()
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de produtos:")
        for produto in produtos:
            print(f"Código: {produto['codigo']} | Nome: {produto['nome']} | Preço: R${produto['preco']:.2f}")
    input("Pressione Enter para continuar...")

def consultar_preco():
    clear_screen()
    codigo = input("Digite o código do produto para consultar o preço: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            print(f"O preço do produto {produto['nome']} é R${produto['preco']:.2f}")
            input("Pressione Enter para continuar...")
            return
    print("Produto não encontrado.")
    input("Pressione Enter para continuar...")

def menu():
    while True:
        clear_screen()
        print("===== Supermercado =====")
        print("1. Inserir novo produto")
        print("2. Excluir produto")
        print("3. Listar produtos")
        print("4. Consultar preço")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            inserir_produto()
        elif escolha == "2":
            excluir_produto()
        elif escolha == "3":
            listar_produtos()
        elif escolha == "4":
            consultar_preco()
        elif escolha == "0":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
