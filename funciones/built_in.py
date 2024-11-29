
numeros = [4, 7, 1, 12, 65, 15]

#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)


#encontrando el numero menor de una lista
numero_mas_chico = min(numeros)
print(numero_mas_chico)

#redondeando a 6 decimales

numero = round(12.345678, 2) #en el segundo parametro le decimos cuantos decimales tienen que tener
print(numero)

#retirna False -> 0, vacio, False, ninguno, lista vacia / True, distinto a 0 o cadena, datos no vacios
resultado_bool = bool(0)
print(resultado_bool)

#all retorna True si todos los valores son verdaderos

resultado_all = all([0, "true", [322,32]]) # si uno solo es falso, devuelve false
print(resultado_all)

suma_total = sum(numeros)
print(suma_total)