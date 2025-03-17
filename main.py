import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar los datos
print("Directorio actual de trabajo:", os.getcwd())  # Verifica el directorio actual
data = pd.read_csv('./data/suicide_rates.csv')  # Ajustar la ruta a 'data/suicide_rates.csv' en Docker y local

# Exploración inicial
print(data.head())
print(data.info())

# Limpieza de datos: manejar valores nulos, convertir tipos, etc.
data = data.dropna()  # Eliminar filas con valores nulos

# Análisis y visualización
plt.figure(figsize=(10,6))
sns.lineplot(data=data, x='year', y='suicides_no')
plt.title('Número de suicidios por año')

# Ruta de salida (local y dentro de Docker)
local_output_dir = './output'  # Carpeta de salida local
docker_output_dir = '/app/volume_output'  # Carpeta de salida en el volumen de Docker

# Crear las carpetas de salida si no existen
os.makedirs(local_output_dir, exist_ok=True)
os.makedirs(docker_output_dir, exist_ok=True)

# Guardar el gráfico en ambas carpetas
plt.savefig(f'{local_output_dir}/suicide_plot.png')  # Guardar en la carpeta local
plt.savefig(f'{docker_output_dir}/suicide_plot.png')  # Guardar en la carpeta del volumen Docker

# Mostrar el gráfico
plt.show()

# Preparación de datos para el modelo
X = data[['year', 'age', 'sex']]  # Características
y = data['suicides_no']  # Variable objetivo

# Convertir categóricas a numéricas (si es necesario)
X = pd.get_dummies(X, drop_first=True)

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Hacer predicciones y evaluar el modelo
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
