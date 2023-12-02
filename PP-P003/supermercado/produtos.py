def cadastrar_novo_produto(estoque):
    print("Digite o código do novo produto")
    codigo = input().zfill(13)
    if any(item["codigo"] == codigo for item in estoque):
        print("Este código já está em uso.")
        return

    print("Digite o nome do produto")
    nome = input().capitalize()
    print("Digite o preço do produto")
    preco = float(input())
    
    novo_produto = {"codigo": codigo, "nome": nome, "preco": preco}
    estoque.append(novo_produto)
    print("Produto cadastrado com sucesso!")



def listar_produtos(estoque):
    produtos_ordenados = sorted(estoque, key=lambda p: p['preco'])
    
    for i, produto in enumerate(produtos_ordenados, start=1):
        print(f"\nProduto {i}:")
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")

        if i % 5 == 0:
            opcao = input("Deseja visualizar mais produtos? (s/n): ").lower()
            if opcao != 's':
                return


def excluir_produto(estoque):
    print("Digite o código do produto a ser removido")
    codigo = input().zfill(13)
    for item in estoque[:]:
        if item["codigo"] == codigo:
            estoque.remove(item)
            print("Produto removido com sucesso.")
            return
    print("Produto não encontrado.")