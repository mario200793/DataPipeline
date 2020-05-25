# Examen DATA PIPELINE
# Mario Fernando Cárdenas Pérez

# Librerias
import requests
import json
# Libreria para delimitar delegaciones mediante poligonos
from shapely.geometry import Point, Polygon
print('Inicio de programa')
# Esta parte del programa la uso para delimitar las delegaciones y crear mis poligonos
if __name__ == '__main__':
    # rows=-1 para que nos de el valor de todas las delegaciones
    url = 'https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=alcaldias&q=&facet=nomgeo&facet=cve_mun&facet=municipio&rows=-1'
    response_delimit = requests.get(url)
    coords=[]
    nombre_alcaldia=[]
    # Si la dirección es correcta procedemos continuamos
    if response_delimit.status_code == 200:
        response_json_delimit = response_delimit.json()
        origen_delimit = response_json_delimit['records']
        # print (origen_delimit[0]['fields']['geo_shape']['coordinates'][0][0])
        # Guardo las coordenadas delimitatorias en mi lista coords
        for j in range(len(origen_delimit)):
            coords.append([])
        for j in range(len(origen_delimit)):
            nombre_alcaldia.append(origen_delimit[j]['fields']['nomgeo'])
            for i in range(len(origen_delimit[j]['fields']['geo_shape']['coordinates'][0])):
                coords[j].append((origen_delimit[j]['fields']['geo_shape']['coordinates'][0][i][0], origen_delimit[j]['fields']['geo_shape']['coordinates'][0][i][1]))

        # Creo lista de poligonos (delegaciones delemitadas)
        poly = []
        for i in range(len(coords)):
            poly.append(Polygon(coords[i]))
        p1 = Point(-103.48899841308594, 0.0)
        p1 = Point(-103.48899841308594, 19.437299728393555)
        p1 = Point(-99.12100219726562, 19.49329948425293)
        # Cin within verifico si esa posicion(punto) se encuentra en el poligono

# Parte de guardar datos
if __name__ == '__main__':
    # &rows nos da el numero de filas, = -1 nos da todas las disponibles
    url = 'https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=prueba_fetchdata_metrobus&q=&rows=-1'
    response = requests.get(url)
    # Si la dirección es correcta continuamos
    if response.status_code == 200:
        # Es un dic, obtengo el json
        response_json = response.json()
        # Origen sera un diccionario con la entrada records de la pagina oficial (acorto)
        origen = response_json['records']
        # Creo mi diccionario con lo que requiero
        dato = {}
        dato['Entrada'] = []
        for i in range(len(origen)):
            p1 = Point( origen[i]['fields']['position_longitude'] , origen[i]['fields']['position_latitude'])
            # Seleccionamos alcaldia
            alcaldia = 0
            for j in range(len(poly)):
                if p1.within(poly[j]) == True:
                    alcaldia = nombre_alcaldia[j]
            if alcaldia == 0:
                alcaldia = "Ubicación Erronea"

            if 'á' in alcaldia:
                alcaldia = alcaldia.replace('á','a')
            if 'é' in alcaldia:
                alcaldia = alcaldia.replace('é','e')
            if 'í' in alcaldia:
                alcaldia = alcaldia.replace('í','i')
            if 'ó' in alcaldia:
                alcaldia = alcaldia.replace('ó','o')
            if 'ú' in alcaldia:
                alcaldia = alcaldia.replace('ú','u')
            dato['Entrada'].append({'id' : origen[i]['recordid'],
                    'fecha' : origen[i]['fields']['date_updated'],
                     'carro' : origen[i]['fields']['vehicle_id'],
                     'longitud' : str(origen[i]['fields']['position_longitude']),
                     'latitud' : str(origen[i]['fields']['position_latitude']),
                     'alcaldia' : str(alcaldia),
            })
        # Guardo el archivo para hacer un historico, solo si la fecha es distinta.

        # Para correrlo la primera vez
        '''
        with open('datos_acumulados.json','w' )as file:
            json.dump(dato,file,indent= 4)
        with open('datos_acumulados2.json','w' )as file:
            json.dump(dato,file,indent= 4)
        '''
        # Leo mi archivo de acumulados y los guardo en data, lo hago para no tener roblemas con json
        # En el archivo1 alamacenamos, todo el historial
        f = open('datos_acumulados.json', 'r')
        data = json.load(f)
        f.close()
        # En el archivo 2 almacenamos los nuevos, estos son los que se almacenaran en la base de datos cada que se corra
        # Base_datos_conector.py

        r = open('datos_acumulados2.json', 'r')
        data2 = json.load(r)
        r.close()
        f1 = open('datos_acumulados.json', 'w')
        f2 = open('datos_acumulados2.json', 'w')
        # Si ya se actualizaron los datos en la pagina, los añadimos a nuestro archivo json
        if data['Entrada'][0]['fecha'] != dato['Entrada'][0]['fecha']:
            json.dump(dato,f2,indent=4)
            for i in range(len(data['Entrada'])):
                dato['Entrada'].append(data['Entrada'][i])
            json.dump(dato,f1,indent= 4)
        # Si los datos no se han atualizado regresamos lo mismos datos que estaban al json
        if data['Entrada'][0]['fecha'] == dato['Entrada'][0]['fecha']:
            json.dump(data,f2,indent= 4)
            json.dump(data,f1,indent= 4)









