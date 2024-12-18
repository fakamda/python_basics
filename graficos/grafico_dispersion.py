import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("graficos\\ingresos.csv")

sns.barplot(x="fuente", y="ingresos", data=df)

total_ingresos = df['ingresos'].sum()

print(f'el total de ingresos es de: {total_ingresos}')

plt.show()