class Model():
    def __init__(self,data):
        self.data = data
    def fit(self,data):
        raise NotImplementedError('Metodo non implementato')
    def predict(self,data):
        raise NotImplementedError('Metodo non implementato')
        
class IncrementModel(Model):
    def predict(self,data):
        if len(data) == 0:
            print("La lista è vuota!!")
            return None
        else:
            n = 0
            for item in data:
                if type(item) != int:
                    print('La lista contiente valori non numerici')
                    return None
                else:
                    n +=1
            i = 0
            somma = 0
            while (i != n-1):
                somma = somma + (data[i+1] - data[i])
                i+=1
            prediction = ((somma/(n-1)) + data[n-1])
            return prediction

class FitIncrementModel(IncrementModel):
    def fit(self,data)

lista = [8,19,31,41,50,52,60]

prediction = IncrementModel(lista)
predizione = prediction.predict(lista)

if predizione != None:
    print(predizione)
            
            