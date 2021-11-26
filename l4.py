class CSVFile():
    def __init__(self, nome):
        self.nome = nome
        
    def get_data(self):
        my_file = open(self.nome,"r")
        lista = []
        for line in my_file:
            lista.append(line.replace("\n",""))
        my_file.close()
        for item in lista:
            print("[{}]".format(item))
       

lista = CSVFile('shampoo_sales.csv') 
lista.get_data()



