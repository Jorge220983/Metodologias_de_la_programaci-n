
"""

String variables

Un string es de manera sencilla una serie 
de caracteres. En python, todo lo que se encuentre 
dentro de comillas simples (' ') o dobles (" ")
sera considerado un string.

Ejemplos:
    "Esto es un string"
    'Esto también es un string'

 ' Le dije a un amigo "Python es mi lenguaje favorito" '
 " El lenguaje 'python' lleva el nombre por Monty Python no por la serpiente "

"""

name = "clase de programación"
print(name)

# title
print(name.title())
print(name)

"""
Un método es una acción que python 
puede realizar en un fragmento de datos 
o sobre una variable.

     El punto . después de una variable 
     seguido del metodo title() dice que 
     se tiene que ejecutar el método title()
     de la variable name.


     Todos los métodos van seguidos de paréntesis 
     porque en ocasiones nesecitan información adicional
     para funcionar. la cual iría dentro de los paréntesis.
     En esta ocasión, el método title() no requiere información 
     adicional para funcionar.


"""

print("Método upper: ", name.upper())
print("Método lower: ", name.lower())

# Concatenación de STRINGS
first_name = "jorge"
last_name = "gonzález"
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())