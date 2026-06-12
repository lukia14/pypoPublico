from database import bd
class UsuarioModel(bd.Model):
    __tablename__ = 'Usuario'

    idUsuario = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    nickname = bd.Column(bd.String(25), nullable=False, unique=True)
    email = bd.Column(bd.String(45), nullable=False, unique=True)
    senha = bd.Column(bd.String(25), nullable = False, unique=False)
    pontuacao = bd.Column(bd.Integer, nullable = False)

    @staticmethod
    def modeloUsuario(form):
        nickname = form.nickname.data
        email = form.email.data
        senha = form.senha.data
        email = form.email.data
        usuario = UsuarioModel(nickname=nickname, email=email, senha=senha)
        return usuario