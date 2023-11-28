def inserir_produto(produtos):
    codigo = input("Digite o código do produto (13 caracteres): ")
    while len(codigo) != 13 or not codigo.isdigit():
        print("Código inválido. Deve conter 13 caracteres numéricos.")
        codigo = input("Digite o código do produto (13 caracteres): ")

    nome = input("Digite o nome do produto (começando com letra maiúscula): ")
    while not nome or not nome[0].isupper():
        print("Nome inválido. Deve começar com uma letra maiúscula.")
        nome = input("Digite o nome do produto (começando com letra maiúscula): ")

    preco = input("Digite o preço do produto (com duas casas decimais): ")
    while not preco.replace('.', '').isdigit():
        print("Preço inválido. Deve ser um número com duas casas decimais.")
        preco = input("Digite o preço do produto (com duas casas decimais): ")

    produtos.append({"codigo": codigo, "nome": nome, "preco": float(preco)})
    print("Produto cadastrado com sucesso!\n")


def excluir_produto(produtos):
    codigo = input("Digite o código do produto a ser excluído: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso!\n")
            return
    print("Produto não encontrado.\n")


def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return

    print("Lista de produtos:")
    for i, produto in enumerate(produtos, 1):
        print(f"{i}. Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")
    print()


def consultar_preco(produtos):
    codigo = input("Digite o código do produto para consultar o preço: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            print(f"O preço do produto {produto['nome']} é R${produto['preco']:.2f}\n")
            return
    print("Produto não encontrado.\n")


def menu():
    produtos = []
    while True:
        print("Menu de Opções:")
        print("1. Inserir novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")
        if opcao == '1':
            inserir_produto(produtos)
        elif opcao == '2':
            excluir_produto(produtos)
        elif opcao == '3':
            listar_produtos(produtos)
        elif opcao == '4':
            consultar_preco(produtos)
        elif opcao == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menu()


