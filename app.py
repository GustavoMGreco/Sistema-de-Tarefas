from flask import Flask
from flask_mysqldb import MySQL
import config


app = Flask(__name__)

app.config.from_object('config')

mysql = MySQL(app)

@app.route('/banco-teste')
def teste():
    try:
        cursor = mysql.connection.cursor()
        
        cursor.execute('SELECT NOW();')
        resultado = cursor.fetchone()

        cursor.close()

        return f'Conexão bem-sucedida! Horário do servidor MySQL:{resultado[0]}'
    except Exception as e:
        return f'Erro ao conectar {e}'
    

if __name__ == ('__main__'):
    app.run(debug=True)