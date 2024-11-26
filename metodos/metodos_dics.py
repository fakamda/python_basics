diccionario = {
    "nombre" : "facundo",
    "apellido" : "dominguez",
    "años" : 26
}

keys = diccionario.keys() #devuelve las claves del dict, tambien sirve para iterar
get = diccionario.get("años") #devuelve el valor de la key que le pasamos si no lo encuentra devuelve None
diccionario.clear() #elimina todo del dict
diccionario.pop("nombre") #elimina un elemento del dict
items = diccionario.items() #con esto podemos iterar los diccionarios


print(items)