class CsvFile:
    def __init__(self,name): # il mio oggetto csvfile
        self.name = name # il nome e' quello che inserisco
        try:
            str(self.name)
        except:
            if not isinstance(self.name,str):
                raise Exception('messaggio di errore, parametro che lo ha generato: "{}", non e\' una stringa')
        try:
            self.csvfile = open(self.name,'r')
        except:
            raise Exception('messaggio di errore, parametro che lo ha generato: "{}", non esiste un file csv con questo nome'.format(self.name))

    def get_data(self,start,end): # metodo get data che stampa la lista dei valori
        try:
            # prova a convertire ad int
            int(start)
            start = int(start) # se tutto va bene salva start come int(start)
        except:
            # alza eccezione, non e' un intero
            raise Exception('messaggio di errore, parametro che lo ha generato: "{}", non e\' un intero.'.format(start))
        try:
           # prova a convertire ad int
            int(end)
            end = int(end)
        except:
            # alza eccezione, non e' un intero
            raise Exception('messaggio di errore, parametro che lo ha generato: "{}", non e\' un intero.'.format(end))
        if(end < start):
            raise Exception('messaggio di errore, parametri che lo hanno generato: "{}","{}", non e\' rispettata la diseguaglianza end >= start'.format(end,start))
        if(start < 1):
            raise Exception('messaggio di errore, parametro che lo ha generato: "{}", start e\' minore di 1'.format(start))
        elif(end < 1):
                raise Exception('messaggio di errore, parametro che lo ha generato: "{}", end e\' minore di 1'.format(end))
        elif(isinstance(start,bool)): # check booleano
            raise Exception('messaggio di errore, parametro che lo ha generato: "{}", non e\' un intero'.format(start))
        elif(isinstance(end,bool)): # check booleano
            raise Exception('messaggio di errore, parametro che lo ha generato: "{}", non e\' un intero'.format(end))
        valori = [] # lista vuota
        for i, line in enumerate(self.csvfile): # per ogni riga del file
            if(i < start-1 or i > end-1):
                continue
            elemento = line.split(',') # crea una lista splittando la riga alla virgola

            if (elemento[0] != 'Date'): # se non è l'intestazione
                data = elemento[0] # set data all'elemento 0
                try:
                    # Provo a convertire elemento[1] a float, se ci riesco allora lo salvo in valore e lo aggiungo alla lista valori
                    float(elemento[1])
                    valore = elemento[1]
                    valori.append(float(valore))
                except:
                    # Se non riesco a convertire elemento[1] a float, alzo un eccezione per avvertire dell'errore e poi salto quel determinato elemento e continuo con il codice
                    print('Non sono riuscito a convertire a float l\'elemento "{}"'.format(elemento[1]))
                    print('Salto questo elemento')
                    continue # Passa al prossimo ciclo
        return valori # Quando ho finito di aggiungere valori alla lista valori stampa tutto)

class Model(object):

    def fit(self,data):
        pass

    def fit(self,prev_months):
        pass

class IncrementModel(Model):

    def fit(self,data):
        raise NotImplementedError('Questo modello non prevede un fit')
    
    def predict(self,prev_months):
        try:
            isinstance(prev_months,list)
        except:
            raise Exception('Errore, prev_months non e\' di tipo lista')
        print("lunghezza lista: {}".format(len(prev_months)))
        if(len(prev_months) < 2):
            raise Exception('prev_months e\' troppo corta, bisogna avere una lista di almeno 2 elementi')

        numero_mesi = len(prev_months)
        incremento = 0
        for i in range(numero_mesi):
            if(i == 0):
                continue
            else:
                incremento += (prev_months[i] - prev_months[i-1])
        
        incremento_medio = incremento / (numero_mesi - 1) # non conto il primo

        return prev_months[-1] + incremento_medio


shampoo_sales = CsvFile("shampoo_sales.csv")
print(shampoo_sales.name)
lista = shampoo_sales.get_data(1,33)
print(lista)
#print(shampoo_sales.get_data(33,39))

test = IncrementModel()
print(test.predict(lista))