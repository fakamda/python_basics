import pandas as pd

df = pd.read_csv("problems\\datos.csv")

# print(df)

#cambiar el tipo de dato de una columna
df['edad'] = df['edad'].astype(str)
# print(df['edad'])

#reemplazar valor
df['nombre'].replace('facundo', 'naruto', inplace=True)
# print(df['nombre'])

df = df.dropna() #elimina las filas que tienen datos vacios si queremos las coluimnas es dropna(axis=1)
# print(df)

#elimina filas repetidas
df = df.drop_duplicates()
print(df)

#creando un csv con un dataframe limpuio

df.to_csv("problems\\datos_limpios.csv")