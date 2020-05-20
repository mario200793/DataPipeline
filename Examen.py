
# Examen DATA PIPELINE
# Mario Fernando Cárdenas Pérez

#Librerias
import requests
import json

#Inicio programa
if __name__ == '__main__':
    # &rows=3 nos da el numero de filas, = -1 nos da todas las disponibles
    url = 'https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=prueba_fetchdata_metrobus&q=&rows=-1'
    response = requests.get(url)
    # Si la dirección es correcta procedemos con el programa
    if response.status_code == 200:
        response_json = response.json() # Es un dic, obtengo el json
        origen = response_json['records']# Origen sera un diccionario con la entrada records de la pagina oficial (acorto)
        # Creo mi diccionario con lo que requiero
        dato = {}
        dato['Entrada'] = []
        for i in range(len(origen)):
            dato['Entrada'].append({'id' : origen[i]['recordid'],
                    'fecha' : origen[i]['fields']['date_updated'],
                     'carro' : origen[i]['fields']['vehicle_id'],
                     'longitud' : str(origen[i]['fields']['position_longitude']),
                     'latitud' : str(origen[i]['fields']['position_latitude']),
            })
        ## Guardo el archivo para hacer un historico, solo si la fecha es distinta.

        # Para correrlo la primera vez
        #with open('datos_acumulados.json','w' )as file:
        #   json.dump(dato,file,indent= 4)
        # Leo mi archivo de acumulados y los guardo en data, lo hago para no tener roblemas con json
        #En el archivo 1 alamacenamos todo el historial
        f = open('datos_acumulados.json', 'r')
        data = json.load(f)
        #Cierro
        f.close()
        #En el archivo 2 almacenamos los nuevos, estos son los que se almacenaran en la base de datos cada que se corra
        # Base_datos_conector.py
        r = open('datos_acumulados2.json', 'r')
        data2 = json.load(r)
        #Cierro
        r.close()
        f1 = open('datos_acumulados.json', 'w')
        f2 = open('datos_acumulados2.json', 'w')
        # Si ya se actualizaron los datos en la pagina, los añadimos a nuestro archivo json
        if data['Entrada'][0]['fecha'] != dato['Entrada'][0]['fecha']:
            json.dump(dato,f2,indent=4)
            for i in range(len(data['Entrada'])):
                dato['Entrada'].append(data['Entrada'][i])
            print (dato)
            json.dump(dato,f1,indent= 4)
        # Si los datos no se han atualizado regresamos lo mismos datos que estaban al json
        if data['Entrada'][0]['fecha'] == dato['Entrada'][0]['fecha']:
            json.dump(data,f2,indent= 4)
            json.dump(data,f1,indent= 4)









