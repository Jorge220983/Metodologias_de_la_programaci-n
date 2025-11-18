# Condiciones numericas 

# Multiple
age_0 = 22
age_1 = 18

print("Multiples Condiciones")
print("Operacion and - pseint (Y)")
print(age_0 >= 21 and age_1 >= 21) # -> False
print(age_0 >= 21 and age_1 >= 18) # -> True 

print("Multiples Condiciones")
print("Operacion or - pseint (O)")
print(age_0 >= 21 or age_1 >= 21) # -> True
print(age_0 >= 21 or age_1 >= 19) # -> False

# ¿Como nos preguntamos si algun valor 
# esta en una lista?
print("\n ¿Esta dentro de la lista?")
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) # -> True
print('pepperoni' in requested_toppings) # -> False

# A value not in a list
print("\n ¿Esta fuera de la lista de baneados?")
banned_users = ["gabriel", "max", "andrik", "quevedo", "christo"]
user = "pedro" 
print(user not in banned_users) # -> True

# Variables de tipo BOOLEANOS
game_active = True
can_edit = False

# If

"""
    if statement

    if condition:
        do something

    if condition
        do something (True)
    else:
        do something (False)
"""

# Preguntar la edad del usuario 
# y decirle si tiene la edad
# suficiente para votar 
# input("") -> str
age =  input("\n\nEscribe tu edad: ")
print(F"\nTu edad es: {age}")

if int(age) >= 18 or age < 99:
    print("Tu tienes la edad suficiente para votar")
else:
    print("Lo siento, eres demasiado joven para votar ")
if int(age) >= 100:
    print("Are you dead")

# Datos booleanos
game_active = True
can_edit = False
