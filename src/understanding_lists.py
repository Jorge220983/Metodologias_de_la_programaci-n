# Lists
"""
   Las listas nos permiten almacenar información 
   en un lugar, la cantidad que tenga: ya sean 
   pocos elementos o millones de elementos.

   Se recomienda nombrar una variable de tipo lista 
   en plural.

   En Python los corchetes [] definen una lista,
   sus elementos van separados por comas. 
   Ejemplo:
"""
bicycle=['trek', 'canondale', 'redline', 'specialized', 'giant']
print(bicycle)

print(bicycle[0].title())

# Los indices comienzan en 0 y terminan en n-1, donde n es el número de elementos
print(bicycle[4].title())

# Accediendo al último elemento
print(bicycle[-1].title()) # ultimo elemento
print(bicycle[-2].title()) # penultimo elemento
print(bicycle[-5].title()) # primer elemento


# Utilizando valores de la lista
message = "Mi primer bicicleta fue una " + bicycle[4].title() + "."
print(message)

message_f = f"Mi primer bicicleta fue una {bicycle[4].title()}."
print(message_f)


## Agregar elementos a una lista
print("\n")
print("Agregar elementos a una lista.")
print(bicycle)

print("Método de las listas para agregar elementos: list_name.append(element)")
bicycle.append("Ducatti")
print(bicycle)
