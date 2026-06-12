from service.FaseService import FaseService
from views.FaseView import FaseView
class FaseController:
    def __init__(self):
        pass
    
    def fase(self,idFase):
        oFaseService = FaseService()
        return oFaseService.fase(idFase)
    
    def material(self,idFase):
        oFaseService = FaseService()
        return oFaseService.material(idFase)
    
    def conclusaoFase(self,pontuacao,idFase):
        oFaseView = FaseView()
        return oFaseView.conclusaoFase(pontuacao,idFase)
    
    def listarFases(self):
        oFaseService = FaseService()
        return oFaseService.listarFases()
    
    def cadastrarFase(self):
        oFaseService = FaseService()
        return oFaseService.cadastrarFase()
    
    def criarFase(self):
        oFaseService = FaseService()
        return oFaseService.criarFase()

    def deletarFase(self, idFase):
        oFaseService = FaseService()
        return oFaseService.deletarFase(idFase)

    def editarFase(self, idFase):
        oFaseService = FaseService()
        return oFaseService.editarFase(idFase)

    def alterarFase(self):
        oFaseService = FaseService()
        return oFaseService.alterarFase()