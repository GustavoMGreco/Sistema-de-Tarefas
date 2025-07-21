from flask import Flask
from extensoes import BD, login_manager
import config
from usuario import buscar_por_id
from flask_login import login_user, login_required, current_user


app = Flask(__name__)

app.config.from_object('config')

BD.init_app(app)

login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/banco-teste')
def teste():
    try:
        cursor = BD.connection.cursor()
        
        cursor.execute('SELECT NOW();')
        resultado = cursor.fetchone()

        cursor.close()

        return f'Conexão bem-sucedida! Horário do servidor MySQL:{resultado[0]}'
    except Exception as e:
        return f'Erro ao conectar {e}'
    

@login_manager.user_loader
def login_usuario(user_id):
    return buscar_por_id(user_id)


@app.route('/teste-login')
def teste_login():
    usuario = buscar_por_id(1)  # ID de teste
    if usuario:
        login_user(usuario)
        return f'Usuário logado: {current_user.nome}'
    return 'Usuário não encontrado'

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Bem-vindo, {current_user.nome}!'
    

if __name__ == '__main__':
    app.run(debug=True)