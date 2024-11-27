edad = 17

if edad >= 18:
    print("podes pasar")
elif edad == 18:  # en python el else if se escribe elif
    print("vemos q onda")
else: 
    print("no podes pasar")

print("esto se ejecuta por fuera del scope")

contraseña = 'PapuFaker2024'
contraseña_escrita= 'PapuFaker2025'

if contraseña == contraseña_escrita: 
    print("todo ok aguante faker")
else: 
    print("todo mal, aguante faker")




ingreso_mensual = 82000
gasto_mensual = 80000

# if anidados
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("tas bien")
    else: 
        print("y, medio dudoso ese manejo")
else:
    print("tamos jodidos")

