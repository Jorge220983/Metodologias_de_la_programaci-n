
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

# Whitespaces

"""
   Un whitespace se refiere a cualquier caracter que no
   se imprime, es decir, un espacio, tabuladores y
   finales de línea. Los whithespaces se utilizan 
   comúnmente para organizar las salidas de tal manera 
   que sea mas amigable de leer o ver para el usuario.
   

   Ejemplo:

      - Tabulador: \t
      - Salto de línea \n
    
"""

print("whitespace Tabulador")
print("Python")
print("\tPython")
print("\t\tPython")

print("Whitespace Salto de línea")
print("Languages: \n\tPython\nC\n\tJavascript")

# Eliminación de espacios en blanco
programming_lenguage = " Python "
print(programming_lenguage)
print(programming_lenguage.rstrip())
print(programming_lenguage.lstrip())
print(programming_lenguage.strip())


# Syntax Error con String
message = "Una fortaleza de python es su comunidad"
print(message)
message = "Una fortaleza de python es su comunidad"
print(message)

# Concatenacíon
first_name = "Jorge"
last_name = "González"
full_name = first_name + last_name
print(full_name)

# f-strings
famous_person = "Hector Gamez" 
message = f"{famous_person} muchas veces dijo que no se durmio que solo estaba cabeceando a compi"
print(message)
print(f"{famous_person.upper()} muchas veces dijo que no se durmio que solo estaba cabeceando a compi")

# Actividad 

"""
Elige el nombre de una persona famosa (quien tu quieras).
Elige una cita famosa de esta persona.
Iguala ambos strings a una variable.

1) Realiza la concatenación utilizando el signo de suma
2) Realiza la concatenación utilizando fstrings

"""
famous_person = "Hector Gamez"
quote = "muchas veces dijo que no se durmio que solo estaba cabeceando a compi"
famous_message = famous_person+ " "+quote
print(famous_person+" "+quote)
print(famous_message)

f_string_message = f"{famous_person} {quote}"
print(f_string_message)
