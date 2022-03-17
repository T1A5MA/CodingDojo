# 1. TASK: print "Hola, mundo"
from posixpath import split


print("Hola, mundo")
# 2. print "Hola Noelle!" con el nombre de una variable
name = "Matias"
print("Hola", name, "!")	# con una coma
print("Hola " + name + "!")	# con un +
# 3. print "Hola 42!" con el número en una variable
num = 72
print("Hola", num, "!")	# con una coma
# print("Hola "+ num + "!")	# con un +	-- ¡esta nos debería arrojar un error!
# 4. print "Amo comer sushi y pizza." con las comidas en variables
fave_food1 = "burritos"
fave_food2 = "pastas"
print("Amo comer {} y {}.".format(fave_food1, fave_food2)) # with .format()
print(f"Amo comer {fave_food1} y {fave_food2}.") # with an f string

### Opcional ###

print("Amo comer %s y %s" % (fave_food1, fave_food2))

text = "Amo comer %s y %s" % (fave_food1, fave_food2)
split_text = text.upper().split()
print(split_text)
