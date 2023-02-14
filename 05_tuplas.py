### Tuples ###

# Definición

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Casa", "Rudy", "Casa")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

# Acceso a elementos y búsqueda

print(my_tuple[0]) #35
print(my_tuple[-1]) #casa
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Casa")) #2  porque tenemos 2 veces casa
print(my_tuple.index("Rudy")) #3 la posicion 3
print(my_tuple.index("Casa")) #2

print()
# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas

print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "zerosdark"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined