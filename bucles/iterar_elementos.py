#en python los bucles son for in

animales = ["perro", "gato", "cocodrilo", "loro"]
numeros = [10, 20, 30, 50] # funciona con tuplas

#iterando animales
for animal in animales:
    print(animal)  

#iterando numeros y multiplicando *10
for numero in numeros:
    resultado = numero*10
    print(resultado)

#iterar 2 listas juntas (necesita la misma cantidad de datos)

for numero, animal in zip(animales, numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")


for numero in range(5, 10): #range le definimos 2 parametros, donde arranca y donde termina
    print(numero)

for numero in range(len(numeros)): #forma no optima de recorrer una lista
    print(numeros[numero])

for num in enumerate(numeros): # el primer valor osea 0 nos da el indice y el 1 el valor
    indice = num[0]
    valor = num[1]
    print(f"el indice es {indice} y el valor es {valor}")

for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino") # utilizando else en for in al final del bucle