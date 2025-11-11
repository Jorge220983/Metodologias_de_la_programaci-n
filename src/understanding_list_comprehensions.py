"""
squares=[]
for value in range(0,11):(
    square = value**2
    squares.append(square)
print(squares)
"""
"""
    Una list comprehention combina el ciclo for 
    y la cfreación de nuevos elementos en una sola 
    línea y automáticamente agrega cada nuevo element
    a la lista, es decir, sin utilizar método append.
"""
squares = [value**2 for value in range(0,11)]
print(squares)

# Para los números pares entre el 0 y el 100
squares_range = [value for value in range(0,101,2)]
print(squares_range)

squares_if = [value for value in range (0,101) if value%2==0]
print(squares_if)
