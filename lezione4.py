class CsvFile:
    def __init__(self,name): # il mio oggetto csvfile
        self.name = name # il nome e' quello che inserisco
        self.csvfile = open(self.name,'r') # apro il file usando il nome

    def get_data(self): # metodo get data che stampa la lista dei valori
        valori = [] # lista vuota
        for line in self.csvfile: # per ogni riga del file
            elemento = line.split(',') # crea una lista splittando la riga alla virgola

            if (elemento[0] != 'Date'): # se non è l'intestazione
                data = elemento[0] # set data all'elemento 0
                valore = elemento[1] # set valore all'elemento 1
            
                valori.append(float(valore)) # aggiungi alla lista valori il valore (elemento[1])
        
        return valori # Quando ho finito di aggiungere valori alla lista valori stampa tutto
shampoo_sales = CsvFile('shampoo_sales.csv')
print(shampoo_sales.name)
print(shampoo_sales.get_data())