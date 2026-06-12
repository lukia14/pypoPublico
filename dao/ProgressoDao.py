from database import bd
from models.ProgressoModel import ProgressoModel

class ProgressoDao:
    def __init__(self):
        pass

    def getProgresso(self,idUsuario):
        progresso = ProgressoModel.query.filter_by(idUsuario=idUsuario).first()
        if progresso:
            return progresso
        else:
            return None
    
    def setProgresso(self,idUsuario,idFase):
        progresso = ProgressoModel.query.filter_by(idUsuario=idUsuario).first()
        progresso.idFase = idFase
        bd.session.commit()

    def criarProgresso(self,idUsuario):
        novoProgresso = ProgressoModel(idUsuario =idUsuario, idFase=1)
        bd.session.add(novoProgresso)