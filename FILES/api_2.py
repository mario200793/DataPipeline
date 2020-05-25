from flask import Flask, render_template, request,jsonify,redirect,url_for
app = Flask(__name__)
import mysql.connector
from mysql.connector import errorcode


config = {
    'user': 'root',
    'password': 'root',
    ## Nos comunicamos con el servicio mysql_db dentro del docker:
    'host': 'mysql_db',
    #El puerto es:
    'port':'3306',
    'database':'DATAPIPELINE',
    'auth_plugin' : 'mysql_native_password',
    'raise_on_warnings': True,
}

# Creamos nuestra ruta raiz donde estara la base de datos completa
@app.route('/')
def index():
    if request.method == "GET":
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM Entrada")
        # ~ cnx.commit()
        # ~ pritn(cursor)
        rows=cursor.fetchall()
        nuevo = {}
        for i in range(len(rows)):
          dentro = {}
          for j in range(len(rows[i])):
            if j == 0:
              dentro['id'] = rows[i][j]
            if j == 1:
              dentro['fecha'] = rows[i][j] 
            if j == 2:
              dentro['carro'] = rows[i][j]            
            if j == 3:
              dentro['longitud'] = rows[i][j]
            if j == 4:
              dentro['latitud'] = rows[i][j]
            if j == 5:
              dentro['alcaldia'] = rows[i][j]                            
          nuevo[i] = dentro
        return jsonify(nuevo)
    return render()
# Obtener una lista de unidades disponibles
@app.route('/unidades')
def index2():
    if request.method == "GET":
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        # query de mysql que da los carros en la ultima hora, que serian los que estan disponibles
        cursor.execute("select carro, COUNT(carro) from Entrada where fecha >= DATE_SUB(NOW(),INTERVAL 1 HOUR) group by carro;")
        rows=cursor.fetchall()
        nuevo = {}
        for i in range(len(rows)):
          dentro = {}
          for j in range(len(rows[i])):
            if j == 0:
              dentro['carro'] = rows[i][j]
            if j == 1:
              dentro['registros'] = rows[i][j]                         
          nuevo[i] = dentro
        return jsonify(nuevo)
    return render()
# Consultar los el historial de ubicaciones/fechas de una unidad dado su ID
@app.route('/historial', methods=['GET','POST'])
def index3():
    if request.method == 'POST':
        carro_n = request.form['carro_n']
        return redirect(url_for('index3_1', carr = carro_n))
    else:
        return render_template('index2.html')
# Obtenemos la query deseada
@app.route('/historial<carr>', methods=['GET','POST'])
def index3_1(carr):
        ccc = mysql.connector.connect(**config)
        cursor = ccc.cursor()
        queryc = "SELECT carro,fecha, latitud, longitud FROM Entrada WHERE carro = \'%s\' " % str(carr)
        cursor.execute(queryc)
        rows1=cursor.fetchall()
        ala = 0
        for i in range(len (rows1)):
            if rows1[i][0] == str(carr):
                ala = 1
        if ala == 0:
            return 'Este carro no esta en la lista'
        if rows1[0][3] == rows1[1][3] and rows1[0][2] == rows1[1][2]:
            return 'Unidad no disponible, no esta en movimiento en la ultima hora'
        print (rows1)
        nuevo = {}
        for i in range(len(rows1)):
          dentro = {}
          for j in range(len(rows1[i])):
            if j == 0:
              dentro['carro'] = rows1[i][j]
            if j == 1:
              dentro['fecha'] = rows1[i][j]
            if j == 3:
              dentro['longitud'] = rows1[i][j]
            if j == 2:
              dentro['latitud'] = rows1[i][j]
          nuevo[i] = dentro
        return jsonify(nuevo)

# Obtener una lista de alcaldías disponibles
@app.route('/alcaldias')
def index4():
    if request.method == "GET":
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute("select alcaldia from Entrada where fecha >= DATE_SUB(NOW(),INTERVAL 1 HOUR) group by alcaldia;")
        # ~ cnx.commit()
        # ~ pritn(cursor)
        rows=cursor.fetchall()
        nuevo = {}
        for i in range(len(rows)):
          dentro = {}
          for j in range(len(rows[i])):
            if j == 0:
              dentro['alcaldia'] = rows[i][j]
          nuevo[i] = dentro
        return jsonify(nuevo)
    return render()
# Obtener una lista de unidades que hayan estado dentro de una alcaldía
#  Elegimos la alcaldia deseada
@app.route('/alcaldia_carro', methods=['GET','POST'])
def index5():
    if request.method == 'POST':
        alcaldia_n = request.form['alcaldia_n']
        return redirect(url_for('indexx', alc = alcaldia_n))
    else:
        return render_template('index.html')
# Obtenemos la query deseada
@app.route('/alcaldia_carro<alc>', methods=['GET','POST'])
def indexx(alc):
        cnx1 = mysql.connector.connect(**config)
        cursor2 = cnx1.cursor()
        print ( alc)
        query = "SELECT alcaldia, carro FROM Entrada WHERE alcaldia = \'%s\'  GROUP BY carro" % str(alc)
        print(query)
        cursor2.execute(query)
        rows=cursor2.fetchall()
        print (rows)
        nuevo = {}
        for i in range(len(rows)):
          dentro = {}
          for j in range(len(rows[i])):
            #if j == 0:
            #  dentro['alcaldia'] = rows[i][j]
            if j == 1:
              dentro['carro'] = rows[i][j]
          nuevo[i] = dentro
        return jsonify(nuevo)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
