def somma_elem_lista(lista):
    sum = 0
    for item in lista:
        sum = sum + item
    print("La somma degli elementi della lista e': {}".format(sum))

lista = [10,10,10]
somma_elem_lista(lista)
