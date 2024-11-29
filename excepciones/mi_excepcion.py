class MiExcepcion(Exception): #se utiliza camel case
    def _init_(self,err):
        print(f"Impresionante, cometiste el siguiente error: {err}")

try:
    raise MiExcepcion("Jjaasdasd")
except:
    print("como vas a hacer eso capo?")