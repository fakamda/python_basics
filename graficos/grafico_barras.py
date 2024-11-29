import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("graficos\\dispersion.csv")

sns.scatterplot(x="tiempo", y="dinero", data=df) # grafico de scatterplot, traza lineas y podemos predecir
# boxplot son para correr graficos de bigotes

plt.show()