### FUNCIONES
# Las funciones son bloque de código para realizar
# una tarea en específico

# Cuando queremos realizar la tarea que se ha definido 
# en la función, tenemos que llamar el nombre de la 
# función que realizar la acción.

""" 
    Sintaxis de una función

    def nomnbre_función():
        acciones
    
    Ejemplo: vamos a definir una función que de un 
    saludo a Christopher
"""
def gretting_christopher():
    """
        Función para saludar a una persona 
        llamada Christopher
    """
    for i in range(0,2):
     print("Hello Christopher")

gretting_christopher()

# Ejemplo de una función que genere el nombre completo 
# de una persona y lo regrese

# parámetros posicionales
def create_full_name(first_name, last_name,  middle_name=""):
   full_name = f"{first_name.strip()} {middle_name.strip()} {last_name.strip()}".title()
   return full_name
user_first_name = input("Dame tu primer nombre: ")
user_middle_name =input("Dame tu segundo nombre (Si no tiene segundo nombre, da enter): ")
user_last_name = input("Dame tu apellido: ")

# argumentos posicionales
generated_fullname = create_full_name(
    user_first_name.lower(), 
    user_last_name.lower(), 
    user_middle_name.lower())
print(generated_fullname)

# argumentos llave
generated_fullname_2 = create_full_name(
   middle_name = user_middle_name,
   first_name = user_first_name,
   last_name = user_last_name
)

