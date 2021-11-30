from datetime import datetime
def somma(my_file):
    somm = 0
    for line in my_file:
        elemento = line.split(',')
        if elemento[0] != 'Date':
            data = elemento[0]
            valore = float(elemento[1])
            somm = somm + valore
    return somm
def lista_date(my_file):
    lista=[]
    for line in my_file:
        elemento = line.split(',')
        if elemento[0] != 'Date':
            data = datetime.strptime(elemento[0],'%d-%m-%Y')
            lista.append(data)
    return lista

my_file = open('shampoo_sales.csv','r')
#somma = round(somma(my_file),1)
#print("La somma dei valori è: {}".format(somma))
lista = lista_date(my_file)
for data in lista:
    print(data.strftime('%d-%m-%Y'))
my_file.close()