archivo = open("archivos\\text.txt", encoding="UTF-8")

#hay que utilizar la codificacion utf8

# archivo_new = archivo.read()
lineas = archivo.readlines() #tambien puede ser readline

archivo.close()

print(lineas)