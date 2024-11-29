with open("archivos\\text.txt","w",encoding="UTF-8") as archivo: # con w si no encuentra el archivo lo crea, tabien lo sobreescribe
    archivo.writelines(["Hola maestro, todo bien?\n", "Rupertosky\n"]) #writelines lo acumula
    archivo.writelines(["Soy un caposky"])
    for i in range(5):
        archivo.write(f'linea {i+1} agregada \n') # usando un bucle