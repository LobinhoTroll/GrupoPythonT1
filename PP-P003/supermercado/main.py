import produtos as p

def main():
    produtos = []
    op = -1
    while(op != 0):
        print("/////////////* MENU */////////////")
        print("1- Inserir Novo Produto")
        print("2- Excluir Produto")
        print("3- Listar Produtos")
        print("4- Consultar Produto")
        print("0- Sair")
        op = int(input())
        match op:
            case 1:
                p.cadastrar_novo_produto(produtos)
            case 2:
                break
            case 3:
                p.listar_produtos(produtos)
            case 4:
                break
    
if __name__ == "__main__":
    main()