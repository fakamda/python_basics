def suma (nombre,*numeros): #el * es args, podemos pasar la cantidad de parametros qe queramos, solo le pasamos a lo ultimo
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("Facundo", 4, 4 , 5, 1) # si le pasamos una lista se puede agregarf

print(resultado)


