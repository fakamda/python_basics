import modulos.modulo_saludar as m #le asignamos nombres 
from modulos.modulo_saludar import saludar #-> con esto podemos importar la funcion particular
from modulos.modulo_saludar import * # >> con este podemos importar todo, no es recomendable

import sys

sys.path.append("ruta")

# import funcion

saludo = m.saludar("Roberto")

print(saludo)

#es mejor utilizar letras mayusculas para las Funciones