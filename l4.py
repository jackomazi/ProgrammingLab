from datetime import datetime
class CSVFile():
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        my_file = open(self.nome,'r')
        return my_file.readline()
        my_file.close()
        
    def get_data(self):
        my_file = open(self.nome,"r")
        lista = []
        for line in my_file:
            lista.append(line.replace("\n",""))
        my_file.close()
        for item in lista:
            print("[{}]".format(item))

    def get_date_vendite(self):
        my_file = open(self.nome,'r')
        lista_date = []
        for line in my_file:
            elemento = line.split(',')
            if elemento[0] != 'Date':
                data = datetime.strptime(elemento[0],'%d-%m-%Y')
                lista_date.append(data)
            my_file.close()
        for data in lista_date:
            print(data.strftime('%d-%m-%Y'))

lista = CSVFile('shampoo_sales.csv')
print (lista)
lista.get_data()
lista.get_date_vendite()


