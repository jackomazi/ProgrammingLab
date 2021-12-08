from datetime import datetime
class CSVFile():
    def __init__(self, nome):
        self.nome = nome
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))
    
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
        return lista

    def get_date_vendite(self):
        file = open(self.nome,'r')
        lista_date = []
        for line in file:
            elemento = line.split(',')
            if elemento[0] != 'Date':
                data = datetime.strptime(elemento[0],'%d-%m-%Y')
                lista_date.append(data)
            file.close()
        for data in lista_date:
            print(data.strftime('%d-%m-%Y'))

lista = CSVFile('shampoo_sales.csv')

print(lista.get_data())
print(lista.get_date_vendite())


