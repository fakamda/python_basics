import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('graficos\\nose.csv')

sns.lineplot(x="fecha", y="nose", data=df)

plt.plot("01-06",122,"o") #creando un punto en el momento mas alto

plt.show()