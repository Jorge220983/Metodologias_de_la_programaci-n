#   Number
"""
     Enteros 
        Los podemos sumar (+), restar (-), 
        multiplicar(*) y dividir (/). 
        Les podemos aplicar potencias(**2, **3, **4, ...), 
        módulo (%)
"""
number_1 = 35
number_2 = 15
suma = number_1 + number_2
resta = number_1 - number_2
multiplicacion = number_1 * number_2
division = number_1/number_2
potencia = number_1**2
modulo = number_1%number_2
print("suma:", suma, type(suma))
print("resta:", resta, type(resta))
print("multiplicacion:", multiplicacion, type(multiplicacion))
print("division:", division, type(division))
print("potencia:", potencia, type(potencia))
print("modulo:", modulo, type(modulo))

"""
   Jerarquía de operaciones
    2 + 3 * 4 -> 14 
   (2 + 3)*4 -> 20
"""

"""
   Floats
        Python llama floats a cualquier número con un punto decimal.

        Los podemos sumar (+), restar (-), 
        multiplicar(*) y dividir (/). 
        Les podemos aplicar potencias(**2, **3, **4, ...), 
        módulo (%)
"""
print(0.1+0.1)
print(0.2-0.2)
print(0.1*2)
print(2*0.2)


# Imprimir la edad de alguien 
age = 18
message = "Jorge tiene " + str(age) + " años."
print(message)
""" 
   TypeError: Esto significa que python 
   no puede reconocer el tipo de información 
   que se esta utilizando.
"""