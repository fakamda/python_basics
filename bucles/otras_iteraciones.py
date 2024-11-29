frutas = ["banana", "manzana", "pera", "ciruela", "naranja", "---"]
string = "Hola ruperstinsky"
numeros = [2, 5, 7, 20]

for fruta in frutas:
    if fruta == 'ciruela': # con esto hacemos que cuando llegue a este elemento lo salte
        continue
    print(f"me voy a comer una {fruta}")


for fruta in frutas:
    if fruta == 'pera': # evitar que el bucle siga ejecutandose
        break
    print(f"me voy a comer una {fruta}")
print("bucle terminado") # cuando termina el bucle en un break no ejecuta el else


#recorrer un string

for letra in string:
    print(letra)

#for en una sola linea de codigo

numeros_duplicados = [x*2 for x in numeros] #expresion matematica
print(numeros_duplicados) 