def somma(my_file):
    somm = 0
    for line in my_file:
        elemento = line.split(',')
        if elemento[0] != 'Date':
            data = elemento[0]
            valore = float(elemento[1])
            somm = somm + valore
    return somm

my_file = open('shampoo_sales.csv','r')
somma = round(somma(my_file),1)
print("La somma dei valori è: {}".format(somma))
my_file.close()