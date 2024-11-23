nombre = "facundo"
nombre = "rupert" #se puede redefinir la variable
print(nombre) 

numero = 1
numero += 1 #suma los numeros
print(numero)

concat = f"hola {nombre} todo bien? {numero}" # --> f string podemos concatenar cualquier valor y lo convierte a texto

print(concat)

del numero # --> operador para borrar datos

# operadores de pertenencia in / not in

print("ola" in concat) # --> si esta devuelve true
print("rubert" not in concat) # --> devuelve true si no esta