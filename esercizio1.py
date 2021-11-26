#funzione che stampa una lista
def stampa(lista):
    for item in lista:
        print(item)
#funzione che stampa somma, media, max e min di una lista di interi
def statistiche(lista):
    somma = 0
    intero = True
    for item in lista:
        if type(item) != int:
            intero = False
            print("La lista conttiene caratteri non interi")
    if intero:
        max = lista[0]
        min = lista[0]
        n = 0
        for item in lista:
                somma = somma + item
                n = n+1
                if item > max:
                    max = item
                if item < min:
                    min = item
        media = somma/n
        print("La somma è: {}\nLa media è: {}\nIl max è: {}\nIl min è: {}\n".format(somma,media,max,min))

#funzione che controlla se ci sono solo interi nella lista
def interi(lista):
    intero = True
    for item in lista:
        if type(item) != int:
            intero = False
    return intero
#funzione somma vettoriale
def somma_vettoriale(lista1,lista2):
    lista3 = []
    interi(lista1)
        
    if interi(lista1) == True and interi(lista2) == True: 
        if len(lista1) == len(lista2):
            for i in range(len(lista1)):
                lista3.append(lista1[i]+lista2[i])
    return lista3

lista1 = [1,2,1,4,100]
lista2 = [2,3,4,5,6,'g']
listastringhe=['Matteo','Marco','Giulia']
stampa(lista1)
stampa(listastringhe)
statistiche(lista1)
lista3 = somma_vettoriale(lista1,lista2)
if len(lista3) == 0:
    print("Le due liste non sono della stessa dimensione oppure contengono elementi non interi.")
else: 
    for item in lista3:
        print(item)