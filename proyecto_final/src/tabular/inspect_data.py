from scipy.io import arff
import pandas as pd

data, meta = arff.loadarff("../data/proyecto_final/tabular/phpnThNfi.arff")
df = pd.DataFrame(data)

print(df.head())
print("\n--- INFO ---")
print(df.info())
print("\n--- COLUMNAS ---")
print(df.columns)