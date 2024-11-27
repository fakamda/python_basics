diccionario = dict(nombre="facundo", apellido="dominguez") # nos pide un key:value

#las listas no pueden ser keys por que son mutables

diccionario2 = {("facundo", "ruperto"): "jaja"} #las tuplas si pueden ser keys, tambien los frozenset

#crear dict con fromkeys() podemos crear con valores none tenemos que pasar de parametro una lista

diccionario3 = dict.fromkeys(["nombre", "apellido"])

print(diccionario, diccionario2, diccionario3)

