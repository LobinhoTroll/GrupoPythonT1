# Importe a classe AnaliseDados e Data 
from AnaliseDados import AnaliseDados
from Data import Data

class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []
                
    def entradaDeDados(self):
        
        qtdItens = 0
        contador = 0
        dataValida = True
        dia = mes = ano = ''

        print("Informe a quantidade de itens na lista: ")
        qtdItens = int(input())

        if qtdItens > 0:
            while contador < qtdItens or not dataValida:
                print("\nInserindo Datas na lista:")
                
                print("\nData", contador + 1, ": ")
                
                dia = int(input("Digite o dia: "))
                mes = int(input("Digite o mês: "))
                ano = int(input("Digite o ano: "))
                
                try:
                    data = Data(dia, mes, ano)
                    self.__lista.append(str(data))
                    contador += 1
                except ValueError as e:
                    print(f"Erro: {e}. Data inválida. Por favor, insira uma data válida.")
                    
            self.ordenar_datas()
                
    def ordenar_datas(self):
        # Converter a lista de strings de datas de volta para objetos Data
        datas_objeto = [Data(int(data.split('/')[0]), int(data.split('/')[1]), int(data.split('/')[2])) for data in self.__lista]

        # Ordenar os objetos Data com base em suas propriedades de data
        datas_objeto.sort()

        # Atualizar a lista com as datas ordenadas em forma de strings
        self.__lista = [str(data) for data in datas_objeto]
                
                               
    
    def mostraMediana(self):
       lista = self.__lista
       mediana = Data
       tamanho = len(lista)
        
       if (tamanho % 2 == 0):
           index = ((tamanho // 2 - 1) + (tamanho // 2)) // 2
           mediana = lista[index]
       else:
           mediana = lista[tamanho // 2]
           
       print("Mediana:" + mediana)
     
    def mostraMenor(self):
        lista = self.__lista
        print("Menor data: " + lista[0])
        
    
    def mostraMaior(self):
        index = len(self.__lista)
        print("Maior data: " + self.__lista[index - 1])
    
    def __str__(self):
        pass
