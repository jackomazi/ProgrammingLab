def somma(lista):
    somm = 0
    for item in lista: somm = somm + item
    print("La somma dei numeri è: {}".format(somm))
lista_num = [1,2,3,4,10]
somma(lista_num)