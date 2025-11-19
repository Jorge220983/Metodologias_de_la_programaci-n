
"""
    Hacer un programa que pregunte la edad de una persona 
    y responda lo siguiente:
        - Si la edad es menor o igual a 4, entonces la entrada
          es gratuita.
        - Si la edad es menor a 18, pero mayor que 4
          entonces la entrada cuesta $200.
        - Si la edad es mayor o igual que 18, entonces la entrada 
          cuesta $400.
"""

try:
    age = int(input("escribe tu edad: "))
except:
    age = -1
    print("Error, ingresaste un caracter no válido")

if age <= 4 and age >= 0:
    print("Entrada gratuita")
elif age < 18 and age > 4:
    print("Tu entrada vale $200")
elif age >= 18:
    print("Tu entrada vale $400")
else:
    print("Tuviste un error")