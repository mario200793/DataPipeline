# Partimos de una base oficial de python

FROM python:3
# El directorio de trabajo es desde donde se ejecuta el contenedor al iniciarse
WORKDIR /FILES
# Copiamos todos los archivos del build context al directorio / del contenedor
ADD . /FILES
COPY . /FILES
# Ejecutamos pip para instalar las dependencias en el contenedor
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Ejecuta nuestra aplicación cuando se inicia el contenedor





