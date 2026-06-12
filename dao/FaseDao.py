from database import bd
from models.FaseModel import FaseModel
class FaseDao:
    def __init__(self):
        pass
    def criarNovaFase(self, form):
        fase = FaseModel(idFase=form.idFase.data, materialApoio=form.materialApoio.data, idModulo=form.idModulo.data, titulo = form.titulo.data)
        bd.session.add(fase)
        bd.session.commit()

    def getFase(self,idFase):
        return FaseModel.query.filter_by(idFase=idFase).first()
    
    def getListaFases(self):
        return FaseModel.query.all()

    def carregarFasePorId(self, idFase):
        return FaseModel.query.get(idFase)

    def deletarFase(self, idFase):
        fase = FaseModel.query.get(idFase)
        if fase:
            bd.session.delete(fase)
            bd.session.commit()

    def alterarFase(self, form):
        idFase = form.idFase.data
        fase_nova = FaseModel(idFase=idFase, materialApoio=form.materialApoio.data, idModulo=form.idModulo.data)
        fase_antiga = FaseModel.query.get(idFase)
        if fase_antiga:
            fase_antiga.materialApoio = fase_nova.materialApoio
            fase_antiga.idModulo = fase_nova.idModulo
            fase_antiga.titulo = fase_nova.titulo
            bd.session.commit()

    def maiorIdFase(self):
        maior = bd.session.query(bd.func.max(FaseModel.idFase)).scalar()
        if maior is None:
            return 1
        else:
            return maior + 1

    def faseExiste(self, materialApoio):
        fase = FaseModel.query.filter_by(materialApoio=materialApoio).first()
        return True if fase else False