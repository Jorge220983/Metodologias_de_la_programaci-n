# Empty Dictionary
homer_0 = {"color": 'yellow', 
        "bag": 'maggie bag', 
        "hair": 'black', "dress": 
        'green', "mom": False,}
print(homer_0)
print(type(homer_0))

marge = {"color": "yellow", 
        'bag': "homer-donut", 
        "hair": 'blue', "dress": 
        'green', "mom": True,}

gun_0 = {"scar": 'yellow-orange', 'headshot': 1.5}

print(homer_0)
homer_0["x-position"]=15
homer_0["y-position"]=25
homer_0["z-position"]=10
print(homer_0)

marge["x-position"]=16
marge["y-position"]=26
marge["z-position"]=10
print(marge)

alien_0 = {"color": 'yellow'}
print(alien_0["color"])

# Modifying an element of dictionary
alien_0["color"] = "Blue"
print(alien_0)

# Adding elements to a dictionary
alien_0["x_position"] = 0 
alien_0["y_position"] = 25
alien_0["name"] = "Paul"

print(alien_0)

# Looping though items
print("\n Looping though items")
for key, value in alien_0.items():
        print(f"The key {key} has value {value}")

# Looping though keys
("\n Looping though keys")
for key in alien_0.keys():
        print(key)

# Looping though values
("\n Looping though value")
for value in alien_0.values():
        print(value)

# NESTING 
# Listas de diccionarios
# Listas en diccionarios
# Diccionarios en diccionarios

