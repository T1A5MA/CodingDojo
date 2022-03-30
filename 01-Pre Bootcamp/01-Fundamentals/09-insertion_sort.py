def insertion_sort(x):
    for i in range(len(x)):
        aux = x[i]
        j = i-1
        print("")
        while j >= 0 and aux < x[j]:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = aux
    return x        

lista = [5, 3, 1, 7 ,4, 9, 6]
print(insertion_sort(lista))

lista = [5, 3, 1, 7 ,4, 6, 9, 2, 8]
print(insertion_sort(lista))