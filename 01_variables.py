#variables
# en camel case para python por convencion no es la manera correcta es snake case
myVariable = "mi variable string en camel case"
print(myVariable)
#por convencion python sugiere snakecase
my_variable ="forma correcta snake case"
print(my_variable)
first_name = 'Rudy'
last_name = "Escalera"
country = 'Bolivia'
city = 'Cercado'
age = 35
is_married = False
skylls = ['HTML','Ruby and Rails','.net','React', 'JS', 'Python' ]
person_info ={
    'first_name' : 'Rudy',
    'last_name' : "Escalera",
    'country' : 'Bolivia',
    'city' : 'Cercado'
}
#imprimiendo los valores  guardadas en las variables
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skylls)
print('Person information: ', person_info)

#casting convertir tipos de datos a otros por medio de funciones de python
# int a float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float a int
gravity = 9.81
print(int(gravity))             # 9

# int a str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'


# str a list
first_name = 'Rudy'
print(first_name)               # 'rudy'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['R','u','d', 'y']

#inputs
nombre = input('cual es tu nombre?')
edad = input('cual es tu edad?')
print(nombre)
print(edad)