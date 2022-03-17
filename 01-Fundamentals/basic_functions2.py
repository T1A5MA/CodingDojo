# 1.
def cuentaRegresiva(x):
    lista = []

    for i in range(x, -1, -1):
        lista.append(i)

    return lista

print(cuentaRegresiva(5))

# 2.
def printAndReturn(x):
    print(x[0])
    return x[1]

output = printAndReturn([1,2])
print(output)

# 3.
def firstPlusLength(x):
    return x[0] + len(x)

print(firstPlusLength([1, 2, 3, 4, 5]))

# 4.
def lengthAndValue(length, value):
    lista = []
    for i in range(length):
        lista.append(value)
    return lista

print(lengthAndValue(4, 7))
print(lengthAndValue(6, 2))

# 5.
def valuesGreaterThanTheSecond(x):
    lista = []
    for i in x:
        if i > x[1]:
            lista.append(i)
    print(len(lista))
    return lista

print(valuesGreaterThanTheSecond([5, 2, 3, 2, 1, 4]))