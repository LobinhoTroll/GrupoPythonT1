from ListaDatas import ListaDatas


def main():
    #nomes = ListaNomes()
    datas = ListaDatas()
    #salarios = ListaSalarios()
    #idades = ListaIdades()

    #listaListas = [nomes, datas, salarios, idades]

    
    datas.entradaDeDados()
    print("___________________")
    datas.mostraMaior()
    print("___________________")
    datas.mostraMenor()
    print("___________________")
    datas.mostraMediana()
    print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
