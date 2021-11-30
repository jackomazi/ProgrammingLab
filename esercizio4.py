class automobile():
    def __init__(self,casa_automo,modello,numero_posti,targa):
        self.casa_automo = casa_automo
        self.modello = modello
        self.numero_posti = numero_posti
        self.targa = targa
    def __str__(self):
        return 'Casa automobile: {}\nModello: {}\nNumero posti: {}\nTarga: {}\n'.format(self.casa_automo,self.modello,self.numero_posti,self.targa)
    def parla(self):
        print('Broom Broom\n')
    def confronta(self,other):
        if self.casa_automo == other.casa_automo and self.modello == other.modello and self.numero_posti == other.numero_posti:
            print('Le due auto hanno le stesse informazioni (tranne, ovviamente, la targa).')
        else:
            print('Le due auto non hanno le stesse informazioni.')

class Transformer(automobile):
    def __init__(self,nometra,generazione,grado,reparto):
        self.nometra = nometra
        self.generazione = generazione
        self.grado = grado
        self.reparto = reparto
    def scheda_militare(self):
        print('Nome: {}\nGenerazione: {}\nGrado: {}\nReparto: {}\n'.format(self.nometra,self.generazione,self.grado,self.reparto))
        
Auto1 = automobile('Peugeot','208','5','AX222HB')
Auto2 = automobile('Volkswagen','Touran','7','AX222HN')
print(Auto1)
print(Auto2)
Auto1.parla()
transformer = Transformer('Optimus Prime','1','capitano','artiglieria pesante')
transformer.scheda_militare()
print(issubclass(Transformer, automobile))
print(type(transformer))
print(type(Auto1))
print(isinstance(Auto1, automobile))
print(isinstance(transformer, automobile))
print(isinstance(Auto1, Transformer))
