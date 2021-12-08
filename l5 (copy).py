class CSVFile:
    def __init__(self, name):

        # Setto il nome del file
        self.name = name
        if type(name) != str:
            raise Exception("Il nome del file non è una stringa!!!")
        
        # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))


    def get_data(self):
        
        if not self.can_read:
            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')
            
            # Esco dalla funzione tornando "niente".
            return None

        else:
            # Inizializzo una lista vuota per salvare tutti i dati
            data = []
    
            # Apro il file
            my_file = open(self.name, 'r')

            # Leggo il file linea per linea
            for line in my_file:
                
                # Faccio lo split di ogni linea sulla virgola
                elements = line.split(',')
                
                # Posso anche pulire il carattere di newline 
                # dall'ultimo elemento con la funzione strip():
                elements[-1] = elements[-1].strip()
                
                # p.s. in realta' strip() toglie anche gli spazi
                # bianchi all'inizio e alla fine di una stringa.
    
                # Se NON sto processando l'intestazione...
                if elements[0] != 'Date':
                        
                    # Aggiungo alla lista gli elementi di questa linea
                    data.append(elements)
            
            # Chiudo il file
            my_file.close()
            
            # Quando ho processato tutte le righe, ritorno i dati
            return data
    def get_data2(self,start = None, end = None):
        if not self.can_read:
            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')
            
            # Esco dalla funzione tornando "niente".
            return None

        else:
            self.start = start
            self.end = end
            try:
            #if ((type(self.start) or type(self.end)) != int):
                int(self.start)
                int(self.end)
                if self.start > self.end:
                    c = self.start
                    self.start = self.end
                    self.end = c
                if self.start<1:
                    self.start=1
                    print("lo start è diventato 1")
                if self.end>37:
                    self.end=37
                    print("lo end è diventato 37")

                data = []

                my_file = open(self.name, 'r')

                cont=1
                for line in my_file:
                    if cont>=self.start and cont <=self.end:
                        data.append(line.replace("\n",""))
                    cont+=1
                my_file.close()
                return data

            except:
                print('Ho avuto un errore!!!')
                print('\nDatisdfs contenuti nel file: "{}"'.format(mio_file.get_data()))
            

mio_file = CSVFile(name='shampoo_sales.csv')
print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data2(39,2)))