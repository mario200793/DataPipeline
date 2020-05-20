
import json

def validador(data):
    try :
        data = json.loads(f.read())
        print ('Si cargo')
        return True
    except ValueError as Error:
        print('No existe')
        return False
f = open('datos_acumulados.json','r' )
validador(f)
