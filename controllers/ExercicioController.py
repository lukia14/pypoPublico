from service.ExercicioService import ExercicioService
from views.ExercicioView import ExercicioView
class ExercicioController:
    def __init__(self):
        pass

    def criarExercicio(self):
        oExercicioService = ExercicioService()
        return oExercicioService.criarExercicio()
    
    def cadastrarExercicio(self):
        oExercicioService = ExercicioService()
        return oExercicioService.cadastrarExercicio()

    
    def listarExercicios(self):
        oExercicioService = ExercicioService()
        return oExercicioService.listarExercicios()
    
    def deletarExercicio(self, idExercicio):
        oExercicioService = ExercicioService()
        return oExercicioService.deletarExercicio(idExercicio)
    
    def editarExercicio(self, idExercicio):
        oExercicioService = ExercicioService()
        return oExercicioService.editarExercicio(idExercicio)
    
    def alterarExercicio(self):
        oExercicioService = ExercicioService()
        return oExercicioService.alterarExercicio()