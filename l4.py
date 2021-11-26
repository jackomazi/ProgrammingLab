class CSVFile():
    def __init__(self, data, valore):
        self.data = data
        self.valore = valore

    def __str__(self):
        return "{},{}".format(self.data,self.valore)
            
my_file = open("shampoo_sales.csv","r")
lista = []
for line in my_file:
    elemento = line.split(',')
    if elemento[0] != 'Date':
        data = elemento[0]
        valore = elemento[1].replace("\n","")
        lista.append(CSVFile(data,valore))


for line in lista:
    print(line)


my_file.close()