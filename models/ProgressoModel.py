from database import bd
class ProgressoModel(bd.Model):
    __tablename__ = 'Progresso'
    idUsuario = bd.Column(bd.Integer, bd.ForeignKey('Usuario.idUsuario'), primary_key=True)
    idFase = bd.Column(bd.Integer, bd.ForeignKey('Fase.idFase'), primary_key=True)

    def __repr__(self):
        return'<Progresso %r>' % self.idUsuario