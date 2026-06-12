from database import bd
class FaseModel(bd.Model):
    __tablename__ = 'Fase'
    idFase = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    titulo = bd.Column(bd.Text,nullable=False)
    materialApoio = bd.Column(bd.Text, nullable=False)
    exercicio = bd.relationship('ExercicioModel', backref='fase', lazy=True)
    idModulo = bd.Column(bd.Integer, bd.ForeignKey('Modulo.idModulo'))
    def __repr__(self):
        return'<Fase %r>' % self.materialApoio


    def __repr__(self):
        return'<Exercicio %r>' % self.exercicio
