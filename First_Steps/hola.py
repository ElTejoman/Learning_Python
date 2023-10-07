import pandas as pd  # importa la librería utilizando el alias pd

# establece la variable file_path utilizando la ruta a nuestros datos csv
file_path = "https://raw.githubusercontent.com/JJTorresDS/ds-data-sources/main/churn_dataset.csv"
df = pd.read_csv(file_path)  # lee los datos csv en el DataFrame df

print(df.head())  # muestra las 5 primeras líneas del DataFrame df