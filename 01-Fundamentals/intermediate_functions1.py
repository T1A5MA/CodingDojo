import random
def randInt(min=0, max=100):

    if min > max:
        return "Debe ingresar un valor máximo mayor que el mínimo"
    if max < 0:
        return "Debe ingresar un valor máximo mayor a cero"

    num = round(random.random() * max + min)
    return num
print(randInt()) 		            # debe imprimir un número entero aleatorio entre 0 y 100
print(randInt(max=50)) 	            # debe imprimir un número entero aleatorio entre 0 y 50
print(randInt(min=50)) 	            # debe imprimir un número entero aleatorio entre 50 y 100
print(randInt(min=50, max=500))     # debe imprimir un número entero aleatorio entre 50 y 500