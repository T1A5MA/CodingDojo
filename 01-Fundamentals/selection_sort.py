def selection_sort(x):
    for i in range(len(x)):
        minVal = x[i]
        minPos = i
        for j in range(i, len(x)):

            if minVal > x[j]:
                minPos = j
                minVal = x[j]

        x[i], x[minPos] = x[minPos], x[i]
    return x
        

lista = [5, 3, 1, 7 ,4, 6, 9]
print(selection_sort(lista))