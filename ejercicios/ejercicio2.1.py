#_falto el profe y los pibes van a armar la clase
#pedir nombre y edad de los compañeros que vinieron a la clase

def obtener_compas(cantidad_de_compas):
    compañeros = []
    for i in range(cantidad_de_compas):
        nombre = input("ingrese el nombre del compa: ")
        edad = int(input("ingrese la edad del compa: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1]) # esto ordena (sort) por el segundo valor de a tupla (edad)
    asistente = compañeros[0][0] #con el primero accedemos al arr y el segundo al valor de la tupla
    profesor = compañeros[-1][0] 

    return asistente, profesor

asistente, profesor = obtener_compas(3)

print(f"El profe es: {profesor} y su asist es {asistente}")