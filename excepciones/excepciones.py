def sumar_dos():
    while True: #inicia bucle
        a = input("Numero 1: ") #pide nums
        b = input("Numero 2: ")
        try:
            resultado = int(a) + int(b) #intenta convertirlos a entero y sumarlo
        except Exception as e: #con esto podemos mostrar cual es el err q ue sucede
            print("basta, capo") #si lanza excepcion te pide ingresar de nuevo
            print(f"Error: {type(e).__name__}")
        else:
            break #si todo salio ok se jecuta el bucle
        finally:
            print("Esto se ejecuta siempre") #manejo de excepcion finalizado
    return resultado

print(sumar_dos())