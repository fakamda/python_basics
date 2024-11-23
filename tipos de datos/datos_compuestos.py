# Listas
lista = ["Roberto", "Carlos", True, 1.80]

print(lista[2]) # --> para acceder a un elemento de la lista 

# tuplas
tupla = ("esto es", 12312, "una tupla", True) #--> las tuplas son listas que no se pueden modificar

print(tupla)
 
# Conjuntos (sets)

set = {"esto es", 123, "un conjunto", False} # no se puede acceder por el indice, ni repetir valores

# diccionario (dict) un json key:value

diccionario = {
 'nombre' : 'facundo',
 'apellido' : 'dominguez',
 'todo bien?' : True,
 'altura' : 1.78,
 'dato duplicado' : 'facundo'
}

print(diccionario['apellido'] + "eda")  #se puede agregar 