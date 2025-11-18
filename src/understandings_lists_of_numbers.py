"""
    Las listas también pueden almacenar 
    números y de hecho, son ideales para esto.
    Python ofrece una gran cantidad de 
    herrramientas que ayudan a trabajar 
    eficientemente listas de números.
"""
# Método built-in range()
"""
    El método range() nos ayuda a crear fácilmente
    series de números.

    Ejemplo 
"""
print("Números del 0 al 9")
for value in range(10): # 10 números entre 0-9
    print(value)
print("Numeros del 1 al 9")    
for value in range(1,10): # 10 números entre 1-9
    print(value)

print("Números Impares del 1 al 9")
for value in range(1,10,2): # 10 números entre 1-9 impares
    print(value)
odd_numbers = list(range(1,10,2))
print(odd_numbers)

print("Números Pares del 1 al 9")
for value in range(2,10,2): # 10 números entre 1-9 pares
    print(value)

print("Tabla del 7")
for value in range(0,71,7): # Tabla del 7
    print(value)
tabla_del_7 = list(range(0,71,7))
print(tabla_del_7)

# Cuadrados de los primeros 10 números
squares = []
for number in range(1,11):
    square = number**2
    squares.append(square)
print(squares)

## Más métodos built-in

# Método min()
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits)) # Salida: 0

# Método max()
digits = [1,2,3,4,5,6,7,8,9,0]
print(max(digits)) # Salida: 9

# Método sum()
digits = [1,2,3,4,5,6,7,8,9,0]
print(sum(digits)) # Salida: 45


