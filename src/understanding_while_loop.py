# While
"""
    El while es un ciclo controlado/comando
    por condición.

    La estructura básica de un while es:

        while conditional:
            actions
"""
# while infinito
"""
    Programa si el usuario escribe números
    entre 25 y 50, entonces estár dentro del rango 
    y salirme de while,
    de otro modo pedirle otro número
"""
while True:
    try:
        number = int(input("Ingresa un número: "))

        if number >= 25 and number <= 50:
            print("Estás en el rango, lo hiciste bien")
            break
        else:
            print("Estas fuera del rango intentalo otra vez")

    except ValueError:
        print("Se ha introducido una variable no válida.")
