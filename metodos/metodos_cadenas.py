string1 = "hola soy facu"
string2 = "bienvenido mastercard"

# print(dir(string1))

# ['__add__', '__class__', '__contains__', '__delattr__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__getnewargs__',
# '__getstate__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__iter__', '__le__',
# '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', 'capitalize', 'casefold',
# 'center', 'count', 'encode', 'endswith', 'expandtabs',
# 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
# 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
# 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
# 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
# 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
# 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
# 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']   

resultado1 = string1.upper() #todo mayus
resultado2 = string1.lower() #todo minus
resultado3 = string1.capitalize() #primera letra mayus
resultado4 = string1.find("a") #encuentra en el string la posicion y -1 cuando no encuentra
resultado5 = string1.index("facu") #si no encuentra nada devuelve una excepcion
resultado6 = string1.isnumeric() #devuelve true si es numerico y false si no
resultado7 = string1.isalpha() #devuelve true si es alfanimerico (de A-Z sin caracteres especiales)
resultado8 = string1.count("a") #devuelve la cantidad de veces que coincide por ejemplo a esta 2 veces
resultado9 = len(string1) #devuelve cuantos caracteres tiene una cadena (no es method es function)
resultado10 = string1.startswith("h") #devuelve true si empieza con lo que le pedimos y false si no 
resultado11 = string1.endswith("u") #devuelve true si termina con lo que le pasamos sino false
resultado12 = string1.replace("hola", "Jelou") #reemplaza el primer parametro con el segundo, una cadena por otra
resultado13 = string1.replace(" ", ",") #podemos reemplazar espacios por comas por ejemplo
resultado14 = string1.split(" ") #cada vez que haya uno de estos parametros nos devuelve un array y los separa, por ejemplo por espacios

print(resultado1, resultado2, resultado3, resultado4, resultado5, resultado6, resultado7, resultado8, resultado9, resultado10, resultado11, resultado12, resultado13, resultado14)
