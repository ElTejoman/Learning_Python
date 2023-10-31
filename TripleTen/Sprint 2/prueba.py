import pandas as pd

# preparamos los datos y los nombres de las columnas
atlas = [
    ["France", "Paris"],
    ["Russia", "Moscow"],
    ["China", "Beijing"],
    ["Mexico", "Mexico City"],
    ["Egypt", "Cairo"],
]
geography = ["country", "capital"]

# creamos un DataFrame
world_map = pd.DataFrame(data=atlas, columns=geography)

# mostrando el DataFrame
print(world_map)
