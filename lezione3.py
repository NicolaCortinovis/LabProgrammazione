my_file = open('shampoo_sales.csv','r') # Apro shampoo_sales.csv in lettura

values = [] # Lista vuota dove andrò a salvare i valori delle vendite

for line in my_file:
    element = line.split(',') # Salvo in una lista gli elementi separati da una virgola in questo caso sono una data ed un valore di vendita

    if(element[0] != 'Date'): # Skip dell'intestazione del file .csv

        data = element[0] # set della data in una variabile dedicata
        valore = element[1] # set del valore in una variabile dedicata

        values.append(float(valore)) # aggiungo un elemento alla lista values

# Ora la mia lista values contiene tutti i valori delle vendite presenti in shampoo_sales.csv

def somma_elementi_lista(lista):
    somma = 0
    for item in lista:
        somma = somma + item
    return somma

print("La somma di tutti i valori delle vendite degli shampoo del file shampoo_sales.csv e' uguale a {}".format(somma_elementi_lista(values)))
    
