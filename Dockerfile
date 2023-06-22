# Utiliza una imagen base con Python instalado
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala los paquetes definidos en requirements.txt
RUN pip install -r requirements.txt

# Copia todo el contenido del proyecto al contenedor
COPY . .

# Expone el puerto en el que se ejecutará el servidor Django
EXPOSE 8000

# Comando para ejecutar el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
