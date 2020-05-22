#Librerias
import requests
import json
# Librerias para base de datos con mysql
import mysql.connector
from mysql.connector import errorcode
## Implemento la conexion con mysql, agregare a la base cada que se tengan nuevos datos
def create_database(cursor,cnx):
    try:
        cursor.execute(
            "CREATE DATABASE {}".format(DB_NAME))
        cnx.commit()
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

config = {
    'user': 'root',
    'password': 'mariooiram',
    'host': '127.0.0.1',
    'auth_plugin' : 'mysql_native_password',
    'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
DB_NAME = 'DATAPIPELINE'
TABLES = {}
# Creo la tabla en mysql
TABLES['Entrada'] = (
    "CREATE TABLE Entrada ("
    "  id varchar(100) NOT NULL,"
    "  fecha varchar(30) NOT NULL,"
    "  carro varchar(30) NOT NULL,"
    "  longitud varchar(30) NOT NULL,"
    "  latitud varchar(30) NOT NULL,"
    "  alcaldia varchar(30) NOT NULL,"
    "  PRIMARY KEY (id)"
    ") ENGINE=InnoDB")

# Creacion de la base, todo lo que tiene que ver con la conexion a mysql
databases = ("SHOW DATABASES")
cursor.execute(databases)
bandera = False
for dbs in cursor:
    if dbs[0] == DB_NAME:
        bandera=True
if bandera:
    cnx.database = DB_NAME
else:
    create_database(cursor,cnx)
    cnx.database = DB_NAME

for name, ddl in TABLES.items():
    try:
        print("Creating table {}:".format(name))
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


add_Entrada = ("INSERT INTO Entrada (id,fecha,carro,longitud,alcaldia,latitud) VALUES(%(id)s, %(fecha)s, %(carro)s, %(longitud)s, %(alcaldia)s, %(latitud)s)")
# Leo mi archivo de acumulados y los guardo en data, lo hago para no tener roblemas con json
f = open('datos_acumulados2.json', 'r')
data = json.load(f)
#Cierro
f.close()
print(data)
## Hago insert a la base de datos
for i in range(len(data['Entrada'])):
    data_Entrada = {
        'id': data['Entrada'][i]['id'],
        'fecha': data['Entrada'][i]['fecha'],
        'carro': data['Entrada'][i]['carro'],
        'longitud': data['Entrada'][i]['longitud'],
        'latitud': data['Entrada'][i]['latitud'],
        'alcaldia': data['Entrada'][i]['alcaldia'],
    }
    cursor.execute(add_Entrada,data_Entrada)
    cnx.commit()

