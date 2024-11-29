diccionario = {
    "nombre" : "facundo",
    "apellido" : "dominguez",
    "años" : 26
}


for key in diccionario: #si iteramos de esta manera solo nos devuelve la key
    print(key)


for items in diccionario.items(): #con items podemos iterar elementos y nos devuelve una tupla
    key = items[0]
    value = items[1]
    print(f"la key es {key} y el value es {value}")



