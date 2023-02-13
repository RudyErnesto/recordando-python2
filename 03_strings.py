#string y funciones
my_string = "mi string"
my_otro_string ="Mi otro String"
print(len(my_string))
print(len(my_otro_string))
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Otra manera de hacer lo mismo
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

#saltros de linea
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # salto de linea
print('Days\tTopics\tExercises') # 4tabs o 4 espacios
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # como se escribe backslash
print('In every programming palabra it starts with \"Hello, World!\"') # como se escribe doble quote en un simple quote

#manejo del contenido del string
palabra = 'python'
primera_letra= palabra[0]
print(primera_letra)
#otra manera de manejar desde la ultima letra
ultimo_letra = palabra[-1]
print(ultimo_letra)
penultima_letra = palabra[-2]
print(penultima_letra)

palabra_slice = palabra[1:3]
print(palabra_slice)

palabra_slice = palabra[1:]
print(palabra_slice)

palabra_slice = palabra[0:6:2]
print(palabra_slice)

# Reverse

reversed_palabra = palabra[::-1]
print(reversed_palabra)

# Funciones del lenguaje

print(palabra.capitalize())
print(palabra.upper())
print(palabra.count("t"))
print(palabra.isnumeric())
print("1".isnumeric())
print(palabra.lower())
print(palabra.lower().isupper())
print(palabra.startswith("Py"))
print("Py" == "py")  # No es lo mismo

