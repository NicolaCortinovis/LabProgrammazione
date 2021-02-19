import csv

class file:
    def __init__(self,name):
        # Salvo il nome dentro l'oggetto
        self.name = name # Salvo il nome dentro l'oggetto


        try:
             # Provo a trasformarlo in una stringa
            str(self.name) 
        except:
            # Se non riesco a trasformarlo in una stringa alzo un eccezione
            raise Exception('Errore, il nome del file "{}" non e\' una stringa'.format(self.name))


        try:
            # Provo ad aprire un file csv avente il nome inserito e lo salvo in una var dentro l'oggetto
            self.csv = open(self.name,'r')
        except:
            # Se non ci riesco non c'è nessun file avente quel nome, alzo eccezione
            raise Exception('Errore, non esiste nessun file avente "{}" come nome'.format(self.name))
        
    
    def get_data(self,start,end):

        ##################################################################################
        ##########################  INIZIO TEST SU START ED END ##########################
        ##################################################################################

        # Controllo che start non sia un booleano
        if(isinstance(start,bool)):
            raise Exception('Errore, start: "{}" e\' un booleano, non un intero'.format(start))

        # Controllo che end non sia un booleano
        if(isinstance(end,bool)):
            raise Exception('Errore, end: "{}" e\' un booleano, non un intero'.format(end))

        # Controllo che start sia passato come intero
        try:
            int(start)
            start = int(start)
        except:
            raise Exception('Errore, start "{}" non e\' convertibile ad intero'.format(start))
        
        # Controllo che end sia passato come intero
        try:
            int(end)
            end = int(end)
        except:
            raise Exception('Errore, end "{}" non e\' convertibile ad intero'.format(end))


        # Controllo che end sia maggiore di start
        if(end < start):
            raise Exception('Errore, il valore di end: "{}" e\' minore del valore di start: "{}"'.format(end,start))
        
        # Controllo che end sia maggiore o uguale a 2 (2 = primo "vero" elemento del csv)
        if(end < 2):
            raise Exception('Errore, il valore di end: "{}" e\' minore di 2, 1 e\' riservato per l\'intestazione del csv'.format(end))

        # Controllo che start sia maggiore o uguale a 2
        if(start < 2):
            raise Exception('Errore, il valore di start: "{}" e\' minore di 2, 1 e\' riservato per l\'intestazione del csv'.format(start))
        
        # Mi calcolo la lunghezza del file csv, e di fatto il numero massimo inseribile come start o end
        reader = csv.reader(self.csv)
        lines= len(list(reader))   

        # Controllo che start non sia maggiore del numero di elementi, se lo e' lo setto al massimo elemento
        if(start > lines):
            print('Errore, il parametro start "{}" superava il numero di elementi presenti nel file csv, e\' stato settato a "{}" ovvero il numero di elementi presenti nel csv'.format(start,lines))
            start = lines
        
        # Controllo che end non sia maggiore del numero di elementi, se lo e' lo setto al massimo elemento
        if(end > lines):
            print('Errore, il parametro end "{}" superava il numero di elementi presenti nel file csv, e\' stato settato a "{}" ovvero il numero di elementi presenti nel csv'.format(end,lines))
            end = lines

        ##################################################################################
        ###########################  FINE TEST SU START ED END ###########################
        ##################################################################################

        self.csv.seek(0) # Ritorniamo in cima al file csv
        valori = []
        for i, line in enumerate(self.csv):
            if(i < start - 1 or i > end - 1):
                continue
            elemento = line.split(',')
            if(elemento [0] != 'Date'):
                try:
                    float(elemento[1])
                    Vendite = float(elemento[1])
                    valori.append(Vendite)
                except:
                    print('Errore, non e\' stato possibile convertire "{}" a float, il valore verra\' saltato'.format(elemento[1]))
                    continue
            
        self.csv.seek(0) # Torniamo in cima
        return valori

class Model(object):
    
    def fit(self,data):
        pass
    
    def predict(self):
        pass

class IncrementModel(Model):
    def fit(self,data):

        if not isinstance(data,list):
            raise Exception('Errore, data non e\' una lista')
        if(len(data) < 2):
            raise Exception('Errore, la lunghezza della lista e\' minore di 2, non e\' possibile operare con liste nulle o aventi solo 1 elemento')

        incremento = 0
        numero_elementi = len(data)

        for i in range(numero_elementi):
            if i == 0:
                continue
            else:
                incremento += (data[i] - data[i-1])
        self.incremento_medio_globale = incremento/(numero_elementi)
        return self.incremento_medio_globale
        
    
    def predict(self,prev_months):
        numero_mesi = len(prev_months)
        incremento = 0
        for i in range(numero_mesi):
            if i == 0:
                continue
            incremento += prev_months[i] - prev_months[i-1]
        
        incremento_medio = incremento/(numero_mesi - 1)
        return (prev_months[-1] + ((incremento_medio/2) + (self.incremento_medio_globale/2)))



Testing = file('shampoo_sales.csv')
print(Testing.name)
tutti_gli_elementi = Testing.get_data(2,40)
print(tutti_gli_elementi[0:30])
Test = IncrementModel()
elementi_fittati = 30
print(Test.fit(tutti_gli_elementi[0:30]))
print(Test.predict(tutti_gli_elementi[0:30]))

