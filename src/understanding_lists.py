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


"""
   Agregar elementos a una lista
       - append(): Agrega un elemento final de la lista.
"""
print("\n--- Agregar elementos a una lista método append() ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']

"""
   Agregar elementos a una lista de posición específica
      - insert(): Inserta un elemento en una posición epecífica.
"""
print("\n--- Elimina un elemento en una posición específica con el método insert() ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']

"""
   Eliminar elementos a una lista
       - del(): Elimina un elemento en una posición específica.
"""
print("\n--- Elimina un elemento en una posición específica con el método del() ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']

"""
  Eliminar elementos a una lista y usar el valor eliminado
       - pop(): Elimina y devuelve el ultimo elemento de la lista.
   
"""
print("\n--- Elimina y devuelve el ultimo elemento de la lista pop() ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
last_motorcycles = motorcycles.pop()
print(motorcycles) # Salida: ['honda', 'yamaha']
print(f'La motocicleta que borraste fue {last_motorcycles}.')

"""
   Eliminar elementos a una lista y usar el valor eliminado
       - pop(index): Elimina y devuelve el ultimo elemento de la lista.
"""
print("\n---  Elimina y devuelve el ultimo elemento de la lista pop(index) ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
last_motorcycles = motorcycles.pop(0)
print(motorcycles) # Salida: ['honda', 'yamaha']
print(f'La motocicleta que borraste fue {last_motorcycles}.')

"""
   Eliminar elementos a una lista por valor
       - remove(): Elimina la primera aparición de un valor específico en la lista.

"""
print("\n---  Elimina un elemento específico de una lista por valor método remove() ---")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles) # Salida: ['honda', 'yamaha', susuki]
print("\n")

"""
   Organizar una lista permanente 
      - sort(): Ordena la lista en orden alfabetica
"""

print("\n--- Organizar una lista permanentemente método sort() ---")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.sort()
print(motorcycles) # Salida: ['ducati', 'honda', 'suzuki', 'yamaha']
print("\n")
motorcycles.sort(reverse=True)
print(motorcycles) # Salida: ['yamaha', 'susuki', 'honda', 'ducati']
print("\n")