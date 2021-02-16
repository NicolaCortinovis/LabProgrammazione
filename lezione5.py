class CsvFile:
    def __init__(self,name): # il mio oggetto csvfile
        self.name = name # il nome e' quello che inserisco
        try:
            self.csvfile = open(self.name,'r')
        except:
            print('Ho avuto un errore, non sono stato in grado di aprire il file di nome: "{}"'.format(self.name))
            print('Non essendoci un file da analizzare, esco dal programma')
            import sys
            sys.exit()

    def get_data(self): # metodo get data che stampa la lista dei valori
        valori = [] # lista vuota
        for line in self.csvfile: # per ogni riga del file
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
        
        return valori # Quando ho finito di aggiungere valori alla lista valori stampa tutto
shampoo_sales = CsvFile('shampoo_sales.csv')
print(shampoo_sales.name)
print(shampoo_sales.get_data())