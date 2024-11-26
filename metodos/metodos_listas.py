lista = list(["hola", "facu", 43]) #podemos crear una lista, buen uso para listas vacias

lista1 = ["hola", "soy", "ruperto"]
lista2 = [5, 2, True, 231, 4, False]

resultado1 = len(lista1) #devuelve la cantidad de elementos de la lista

lista1.append("JUJU") #agregamos elemento con append, lo agrega a la lista original

lista1.insert(2, "pepito") #agrega un elemento a la lista en la posicion que le decimos

lista1.extend([False, 2040]) #extend agrega una lista a la lista original

lista1.pop(0) #elimina un elemento de la lista por su indice 
lista1.pop(-1) #con -1 elimina el ultimo -2 el anteultimo

lista1.remove("ruperto") #elimina un elemento de la lista por su valor, si no lo encuentra devuelve excepcion

lista1.clear() #elimina todos los elementos

lista2.sort() #ordena elementos de manera ascendente primero False, True y luego numeros ASC
lista2.sort(reverse=True) #ordena los elementos pero al reves, de manera DESC
lista1.reverse() #devuelve de manera invertida cualquier lista

print(lista1, lista2) 

#PARA TUPLAS SOLO PODEMOS USAR INDEX Y COUNT, O LEN

#PARA SETS PODEMOS SACAR Y REMOVER ELEMENTOS PERO NADA MAS