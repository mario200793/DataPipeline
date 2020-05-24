from flask import Flask, render_template, request,jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'mysql_db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'DATAPIPELINE'

mysql = MySQL(app)


@app.route('/')
def index():
    if request.method == "GET":
        details = request.form
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Entrada")
        rows=cur.fetchall()
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

@app.route('/unidadesdisponibles')
def index2():
    if request.method == "GET":
        details = request.form
        cur = mysql.connection.cursor()
        cur.execute("SELECT carro, COUNT(carro) FROM Entrada GROUP BY carro")
        rows=cur.fetchall()
        nuevo = {}
        for i in range(len(rows)):
          dentro = {}
          for j in range(len(rows[i])):
            if j == 0:
              dentro['carro'] = rows[i][j]
            if j == 1:
              dentro['# de registros'] = rows[i][j]
          nuevo[i] = dentro
        return jsonify(nuevo)
    return render()
    
@app.route('/historial')
def index3():
    if request.method == "GET":
        details = request.form
        cur = mysql.connection.cursor()
        cur.execute("SELECT carro, COUNT(carro) FROM Entrada GROUP BY carro")
        rows=cur.fetchall()
        nuevo = {}
        for i in range(len(rows)):
          dentro = {}
          for j in range(len(rows[i])):
            if j == 0:
              dentro['carro'] = rows[i][j]
            if j == 1:
              dentro['# de registros'] = rows[i][j]
          nuevo[i] = dentro
        return jsonify(nuevo)
    return render()
    
@app.route('/alcaldias')
def index4():
    if request.method == "GET":
        details = request.form
        cur = mysql.connection.cursor()
        cur.execute("SELECT carro, COUNT(carro) FROM Entrada GROUP BY carro")
        rows=cur.fetchall()
        nuevo = {}
        for i in range(len(rows)):
          dentro = {}
          for j in range(len(rows[i])):
            if j == 0:
              dentro['carro'] = rows[i][j]
            if j == 1:
              dentro['# de registros'] = rows[i][j]
          nuevo[i] = dentro
        return jsonify(nuevo)
    return render()


@app.route('/alcaldias_unidades')
def index5():
    if request.method == "GET":
        details = request.form
        cur = mysql.connection.cursor()
        cur.execute("SELECT carro, COUNT(carro) FROM Entrada GROUP BY carro")
        rows=cur.fetchall()
        nuevo = {}
        for i in range(len(rows)):
          dentro = {}
          for j in range(len(rows[i])):
            if j == 0:
              dentro['carro'] = rows[i][j]
            if j == 1:
              dentro['# de registros'] = rows[i][j]
          nuevo[i] = dentro
        return jsonify(nuevo)
    return render()

if __name__ == '__main__':
    app.run(host='localhost', port=8002, debug=True)
