# Exploración de Datos

En este paso, analizamos la estructura del dataset y realizamos una exploración preliminar.

## Carga de los Datos
El dataset se carga desde el archivo `suicide_rates.csv`. Utilizamos `pandas` para inspeccionar las primeras filas y entender la estructura:

```python
import pandas as pd
data = pd.read_csv('./data/suicide_rates.csv')
print(data.head())
