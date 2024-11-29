import pandas as pd

df = pd.read_csv("archivos\\datos.csv", names=["name", "lastname", "age"]) #df es dataframe
df2 = pd.read_csv("archivos\\datos.csv", names=["name", "lastname", "age"])
# print(df["name"]) #obteniendo los datos de nombre

# string = "0123456789"

# print(string[2:7]) #el : es slicing, le pedimos desde donde comienza hast adonde termina  por ejemplo 2:9 empieza en 2 y termina en 9

#ordenar df por edad
df_ordenado = df.sort_values("age", ascending=False) #crea un valor anonimo asi que lo tenemos que asignarlo a una variable, para ordenarlo desc tenemos que usar ascending=False
# print(df_ordenado)

#concatenando 2 df
df_concatenado = pd.concat([df,df2])

# print(df_concatenado)

#accediendo a la primer fila
primer_fila = df.head(2)

#accediendo a la ultima fila
ultima_fila = df.tail(2)

#accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape 

#obteniendo data estadistica del df
df_info = df.describe()

#accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[2, "age"]

#accediendo con iloc
elemento_especifico_iloc = df.iloc[2, 2] # esto accede por indice y no por value

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1] #con slicing le pedimos todos los elementos 

#accediendo a fuilas con loc
fila_3 = df.loc[2, :]


# mayor_que_30 = df.loc[df["age"],:]
# print(mayor_que_30)

