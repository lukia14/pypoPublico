from sqlalchemy import func
from database import  bd
from models.ExercicioModel import ExercicioModel
class ExercicioDao:
    def __init__(self):
        pass

    def criarNovoExercicio(self,form):
        exercicio = ExercicioModel.modeloExercicio(form)
        bd.session.add(exercicio)
        bd.session.commit()
    
    
    def carregarExercicios(self):
        exercicios = ExercicioModel.query.all()
        return exercicios
    
    def carregarExercicioPorId(self, idExercicio):
        exercicio = ExercicioModel.query.get(idExercicio)
        return exercicio
    
    def deletarExercicio(self, idExercicio):
        exercicio = ExercicioModel.query.get(idExercicio)
        if exercicio:
            bd.session.delete(exercicio)
            bd.session.commit()

    def alterarExercicio(self,form):

        exercicio = ExercicioModel.modeloExercicio(form)

        exercicioAntigo = ExercicioModel.query.get(exercicio.idExercicio)
        if exercicioAntigo:
            exercicioAntigo.numero = exercicio.numero
            exercicioAntigo.titulo = exercicio.titulo
            exercicioAntigo.enunciado = exercicio.enunciado
            exercicioAntigo.resposta = exercicio.resposta
            exercicioAntigo.idFase = exercicio.idFase
            exercicioAntigo.alternativaA = exercicio.alternativaA
            exercicioAntigo.alternativaB = exercicio.alternativaB
            exercicioAntigo.alternativaC = exercicio.alternativaC
            exercicioAntigo.alternativaD = exercicio.alternativaD
            bd.session.commit()
    
    #funcoes auxiliares
    def maiorIdExercicio(self):
        maiorId = bd.session.query(func.max(ExercicioModel.idExercicio)).scalar()
        if maiorId is None:
            return 1
        else:
            return maiorId + 1
    def exercicioExiste(self,enunciado):
        exercicio = ExercicioModel.query.filter_by(enunciado=enunciado).first()
        if exercicio:
            return True
        else:
            return False
        
    
        