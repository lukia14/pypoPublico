from database import bd
class ExercicioModel(bd.Model):
    __tablename__ = 'Exercicio'
    idExercicio = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    titulo = bd.Column(bd.String(25), nullable=False)
    enunciado = bd.Column(bd.Text, nullable=False)
    alternativaA = bd.Column(bd.String(99), nullable=False)
    alternativaB = bd.Column(bd.String(99), nullable=False)
    alternativaC = bd.Column(bd.String(99), nullable=False)
    alternativaD = bd.Column(bd.String(99), nullable=False)
    resposta = bd.Column(bd.Text, nullable=False)
    idFase = bd.Column(bd.Integer, bd.ForeignKey('Fase.idFase'), nullable=False)
    numero = bd.Column(bd.Integer, nullable=False)

    def __repr__(self):
        return'<Exercicio %r>' % self.titulo
    
    @staticmethod
    def modeloExercicio(form):
        idExercicio = form.idExercicio.data
        titulo = form.titulo.data
        enunciado = form.enunciado.data
        alternativaA = form.alternativaA.data
        alternativaB = form.alternativaB.data
        alternativaC = form.alternativaC.data
        alternativaD = form.alternativaD.data
        resposta = form.resposta.data
        idFase = form.idFase.data
        numero = form.numero.data

        exercicio = ExercicioModel(
            idExercicio=idExercicio,
            titulo=titulo,
            enunciado=enunciado,
            alternativaA=alternativaA,
            alternativaB=alternativaB,
            alternativaC=alternativaC,
            alternativaD=alternativaD,
            resposta=resposta,
            idFase=idFase,
            numero=numero
        )
        return exercicio