from flask_login import UserMixin
from extensoes import BD


class Usuario(UserMixin):
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

def buscar_por_id(id):
    cursor = BD.connection.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE id = %s', (id,))
    res = cursor.fetchone()
    if res:
        return Usuario(*res)
    return None
