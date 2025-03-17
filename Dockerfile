# Usar una imagen base con Python
FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de dependencias
COPY requirements.txt requirements.txt

# Instalar las librerías necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos al contenedor
COPY . .

# Comando por defecto al iniciar el contenedor
CMD ["python", "main.py"]
