frase = input("Decime algo y calculo cuanto tardarias si tuvieras que decirla:  ")

palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Facu tardaria {cantidad_de_palabras/2*1.3} segundos')
if cantidad_de_palabras > 10:
    print("Para maestro tampoco te pedi un testamento")
