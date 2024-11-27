#creando un conjunto con set

conjunto = set(["dato1", ("datolista1", "datolista2")]) # no se le puede pasar datos mutables por ejemplo listas, pero si tuplas

conjunto1 = {"dato1", "dato2"}
# conjunto2 = {conjunto, "dato3"} # no se puede meter un conjunto dentro de otro conjunto d eesta manera

conjunto3 = frozenset(["dato1", "dato2"]) #con frozenset si
conjunto4 = {conjunto3, "dato3"}

print(conjunto4)

# TEORIA DE CONJUNTOS

# TENEMOS UN CONJUNTO Y UN SUBCONJUNTO

# SI EN B tenemos {2 4 6 8 10} y en A tenemos {2 4 6}, a es un subconjunto de B 

# mientras que B es un superconjunto de B

conjunto5 = {1,3,5,7}
conjunto6 = {1,3,7}

resultado = conjunto6.issubset(conjunto5) #conjunto 6 es subconjunto de 5? si por que 6 tiene menos num
resultado2 = conjunto5.issuperset(conjunto6) # conjunto 5 es superset de conjunto 6 ya que tiene mas num

resultado3 = conjunto6 <= conjunto5 # otra manera de decir subset
resultado4 = conjunto5 > conjunto6 # otra manera de decir superset

resultado5 = conjunto6.isdisjoint(conjunto5) #es true solo cuando los conjuntos no tienen ningun numero igual

print(resultado, resultado2, resultado3, resultado4, resultado5)