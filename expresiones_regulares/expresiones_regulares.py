import re

texto = '''Hola maestro, esta es la cadena 111. como estas mi capitan
Esta es la segunda linea de texto. ?? - $
Y Esta es la final definitiva mi capitan 2224 ab abb abbb abab ababab
23/06/2024 
'''

# resultado = re.search("Hola", texto) #este encuentra el primer hola
# resultado = re.findall("Esta", texto, flags=re.IGNORECASE) # re.ignorecase ignora las case
# print(resultado)

# \d --> busca digitos numericos del 0 - 9
# \D  --> busca TODO menos digitos numericos del 0 - 9
# \w --> busca caracteres alfanuimericos [a-z A-Z 0-9 _]
# \W --> busca TODO menos los caracteres alfanumericos [' ' \n]
# \s --> busca espacios en blancos --> espacios, tabs, saltos de linea
# \S --> busca TODO menos espacios en blanco
# \n --> busca todos los saltos en linea
# . --> busca TODO menos saltos en linea
# ^ -->busca el principio de una linea
# $ -->busca el final de una linea
# {n} --> busca n cantidad de veces el valor de la izq
# {n,m} --> busca n cantidad de veces y como maximo m

# \ --> cancela caracteres especiales [?-] por ejemplo \? \. \, y asi
# * --> si encuentra 0 coincidencias te lo perdona y si encuentra 1 devuelve todos
# resultado = re.findall(r"\?", texto)
# con / busca una barra
# con + busca una coincidencia

#Armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r'\d\.\s', texto)

resultado = re.findall(r"capitan$", texto, flags=re.M) #con re.M el comienzo de cada linea se guia por el salto de linea


resultado = re.findall(r"\d{3,4}", texto, flags=re.M) #busca que haya 3 numeros del 0 al 9 seguidos y un maximo de 4, si supera lo corta

resultado = re.findall(r"(ab){2}", texto) #si encuentra el texto {n} cantidad de veces, lo devuelve
resultado = re.findall(r"[ab]{2}", texto) #devuelve n cantidad de veces si encuentra cualquiera de los 2 aunque sea invertidos
resultado = re.findall(r"\d{2.4}|Hola", texto) #es un or, el que encuentra primero devuelve

pattern = r'\d{2}/\d{2}/\d{4}'
replacement = 'Fecha Oculta'

resultado = re.sub(pattern, replacement, texto) #buscar una fecha

re.sub #--> encuentra un patron y lo reemplaza

pattern_mail = '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z{2,}]' #
pattern_mail_casilla = r'[a-zA-Z0-9._%+-]+@facundo\.[a-zA-Z]{2,}' #en este caso busca el patron si contiene o no @facundo.algo

pattern_http = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
re.match #---> verifica si coincide

print(resultado)