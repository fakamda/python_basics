numeros = [1,2,3,4,5,6,7,8,9]

multiplicar_por_dos = lambda x : x*2 #con lambda podemos hacer funciones anonimas

# print(multiplicar_por_dos(5))
#beneficios: sencillo, rapido, retorna automaticamente, no son aptas para mas de una instruccion

#usando filter con una funcion comun
# def es_par(num):
#     if(num%2==0):
#     # if(num%2==1): # esto es para numeros impares
#         return True
    
# numeros_pares = filter(es_par, numeros)

# print(list(numeros_pares))


# creando lo mismo con lambda

numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
print(list(numeros_pares))