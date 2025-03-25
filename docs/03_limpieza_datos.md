#### 3. `03_limpieza_datos.md`
Detalla los pasos de limpieza de los datos, como la eliminación de valores nulos y la conversión de tipos de datos.

```markdown
# Limpieza de Datos

El dataset contiene valores nulos, por lo que se realizó una limpieza de datos para eliminar filas con valores faltantes.

```python
data = data.dropna()  # Eliminamos las filas con datos faltantes
