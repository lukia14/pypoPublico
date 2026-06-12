from database import bd
class ModuloModel(bd.Model):
    __tablename__ = 'Modulo'
    idModulo = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    numero = bd.Column(bd.Integer, nullable=False)
    nome = bd.Column(bd.String(25), nullable=False, unique=True)
    idMundo = bd.Column(bd.Integer, bd.ForeignKey('Mundo.idMundo'))
    fase = bd.relationship('FaseModel', backref='modulo', lazy=True)

    def __repr__(self):
        return'<Modulo %r>' % self.nome
