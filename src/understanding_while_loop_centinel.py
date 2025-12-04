"""
    Docstring  for understanding_while_loop_centinel

    Un programa que:
        - Cuente cuantos numeros ha ingresado el usuario.
        - Realice la suma de estos numeros 
        - Me diga cual es el minimo de los numeros ingresados 
        - Me diga cual es el maximo de los numeros ingresados 
"""
counter = 0
sum_quantities = 0.0
minimum = None
maximum = None

while True:
    print("Escribe exit para salir")
    user_input = input("Ingresa una cantidad (MXN): ")

    if user_input == 'exit':
        break

    try:
        value = float(user_input)
    except ValueError:
        print("Caracter invalido. Porfavor ingresa un numero")
    except KeyboardInterrupt:
        print("Salida manual")
        break
    
    counter+=1 # counter = counter + 1 (contador)
    sum_quantities += value # sum_quantities = sum_quantities + value (sumador)

    if minimum is None or value < minimum: 
        minimum = value
    
    if minimum is None or value > minimum: 
        maximum = value

print("Cantidad de numeros ingresados", counter)
print("Suma de cantidades ", sum_quantities)
print("Minimo de cantidades", minimum)
print("Maximo de cantidades", maximum)
