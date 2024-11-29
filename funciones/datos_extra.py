# #creando una funcion de 3 parametros
# def frase(nombre, apellido, adjetivo):
#     return f'hola {nombre} {apellido}, sos muy {adjetivo}'

# #utilizando keywords arguments
# frase1 = frase(adjetivo = "groso", nombre = "facundo", apellido = "dominguez")


#parametro opcional por defecto
def frase(nombre, apellido, adjetivo = "Tonto"):
    return f'hola {nombre} {apellido}, sos muy {adjetivo}'

#utilizando keywords arguments
frase1 = frase(nombre = "facundo", apellido = "dominguez") # si no le pasamos parametro agarra el predefinido, en cambio, podemos redefinir un parametro pre-definido

print(frase1)