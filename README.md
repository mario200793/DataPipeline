# DataPipeline
Prueba DataPipeLine

MARIO

Esta prueba se hizo con Python3, FLASK y MySQL:8.0.20.

Para la coneccion con 

Se empaqueto con docker.

Instrucciones:

$ sudo docker pull mysql

$ sudo docker-compose up

$ sudo docker-compose exec redis bash

Una vez dentro del bash de redis, ejecutar:

    python3 Examen.py

    python3 Base_datos_conector.py

    python3 api_2.py


Entrar a localhost:8082 desde tu navegador (Tener libre el puerto 8082 de tu maquina)

○ Obtener una lista de unidades disponibles

localhost:8082/unidades

○ Consultar los el historial de ubicaciones/fechas de una unidad dado su ID

localhost:8082/historial

○ Obtener una lista de alcaldías disponibles

localhost:8082/alcaldias

○ Obtener una lista de unidades que hayan estado dentro de una alcaldía

localhost:8082/alcaldia_carro

