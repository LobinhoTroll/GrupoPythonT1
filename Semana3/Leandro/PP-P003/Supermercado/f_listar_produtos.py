from Supermercado.f_inserir_produto import listaDeProdutos


def listaProdutos():

    listaDeProdutos.sort(key=lambda x: float(x['preco']))

    print("Produtos ordenados por preço crescente: ")
    print("----------------------------------------")
    for produto in listaDeProdutos:
        print("Código: " + produto['codigo'] )
        print("Nome: " + produto['nome'] )
        print("Preço: " + produto['preco'] )
        print(" ")
        
    
