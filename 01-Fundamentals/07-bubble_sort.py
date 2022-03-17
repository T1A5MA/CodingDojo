def bubble_sort(x):
    i=0
    for j in range(len(x)-1):
        for i in range(len(x)-j-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    return x

lista = [5, 3, 1, 7 ,4, 6, 9]
print(bubble_sort(lista))