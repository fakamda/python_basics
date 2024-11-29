
# #creando una funcion simple
# def saludar():
#     print("Hola facu, como estas")
# #ejecutando la funcion simple
# saludar()

#creando una funcion con params
def saludar(nombre, sexo):
    sexo = sexo.lower() #esto se hace para que si el parametro sea mayus o minus siempre sea lower

    if (sexo == "mujer"):
        adjetivo = "reina"

    elif (sexo == "hombre"):
        adjetivo = "titan"

    else:
        adjetivo = "queridx"

    print(f"hola {nombre}, {adjetivo} como andas")

saludar("Facu", "Hombre") # le pasamos los parametros.
saludar("Rocio", "mujer") 
saludar("ruperto", "no binario")


#--------------------------------------------------------------
# crear una funcion que retorne values

def crear_pass(num):
    chars = "abcdefghij"
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña, num #return, esto es un valor que podemos asignarle a otras cosas / tambien podemos retornar una tupla

password, primer_num = crear_pass(242)
frase = f"tu pass nueva es : {password} y el  numero que se utilizo fue {primer_num}"
print(frase)