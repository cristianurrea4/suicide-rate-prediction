
# Análisis y Predicción de Tasas de Suicidio

Este proyecto tiene como objetivo analizar y predecir las tasas de suicidio a lo largo de los años, utilizando un conjunto de datos históricos sobre suicidios. Se emplean técnicas de análisis de datos, visualización y modelos de machine learning para predecir las tasas de suicidio en función de diferentes variables, como el año, la edad y el sexo.

## Descripción

Este proyecto utiliza el conjunto de datos **Suicide Rates Overview 1985 to 2016** para realizar un análisis exploratorio de los datos, limpiar los datos y generar visualizaciones. Luego, se crea un modelo de regresión lineal para predecir las tasas de suicidio en función de las características proporcionadas.

### Tecnologías Utilizadas

- **Python**: Lenguaje principal de programación utilizado.
- **Pandas**: Para la manipulación de datos.
- **Matplotlib / Seaborn**: Para la visualización de los datos.
- **Scikit-learn**: Para la creación y evaluación del modelo de machine learning.
- **Docker**: Para crear un contenedor que ejecute el análisis en un entorno aislado.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
suicide_analysis/
│
├── data/
│   └── suicide_rates.csv           # Conjunto de datos sobre las tasas de suicidio
│
├── docs/
│   ├── 01_introduccion.md          # Introducción del proyecto
│   ├── 02_exploracion_datos.md     # Análisis exploratorio de los datos
│   ├── 03_limpieza_datos.md        # Proceso de limpieza de datos
│   ├── 04_visualizaciones.md       # Visualización de los datos
│   ├── 05_modelo_predictivo.md     # Creación y evaluación del modelo predictivo
│   └── 06_conclusiones.md          # Conclusiones del proyecto
│
├── output/
│   └── suicide_plot.png            # Gráfico generado durante el análisis
│
├── Dockerfile                      # Configuración de Docker para crear el contenedor
├── docker-compose.yml              # Orquestación de Docker
├── main.py                         # Script principal para ejecutar el análisis
├── requirements.txt                # Dependencias del proyecto
└── README.md                       # Este archivo
```

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalados los siguientes paquetes:

- Python 3.9+
- Docker (opcional, pero recomendado para ejecutar en un contenedor aislado)

Puedes instalar las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar el proyecto con Docker

1. **Construir la imagen Docker**:
   
   ```bash
   docker-compose build
   ```

2. **Ejecutar el contenedor**:
   
   ```bash
   docker-compose up
   ```

Esto ejecutará el análisis y generará un gráfico sobre la tasa de suicidio que se guardará en la carpeta `output/`.

### Ejecutar el proyecto localmente

Si prefieres ejecutar el proyecto sin Docker, puedes hacerlo directamente en tu entorno local.

1. Clona el repositorio:

   ```bash
   git clone https://github.com/cristianurrea4/suicide-rate-prediction.git
   cd suicide-rate-prediction
   ```

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta el script principal:

   ```bash
   python main.py
   ```

El gráfico generado se guardará en la carpeta `output/` y se mostrará en tu pantalla.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request describiendo tus cambios.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

Si tienes alguna duda o sugerencia, no dudes en abrir un **issue** o enviar un **pull request**.

¡Gracias por tu interés en este proyecto!
