# Lista vacia 
guisos = []
if guisos:
    print("Hay guisos")

# Utilizando varias listas 
guisos_disponibles = ['salsa verde', 'deshebrada', 'mole']
guisos_a_ordenar = ['deshebrada', 'caldo de iguana']

print("¿Qué guiso desea ordenar?")
for guiso in guisos_a_ordenar:
    print(f"Deseo{guiso}")
    if guiso in guisos_disponibles:
        print(f"Si tenemos {guiso}")
    else:
        print("No tenemos de ese guiso")
print("Realizando pedido...")

