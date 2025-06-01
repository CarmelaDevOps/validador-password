# Imagen base oficial de Python
FROM python:3.10

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el script al contenedor
COPY validador.py .

# Comando por defecto al iniciar el contenedor
CMD ["python", "validador.py"]

