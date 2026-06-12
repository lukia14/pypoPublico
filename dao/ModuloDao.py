from database import bd
from models.ModuloModel import ModuloModel
class ModuloDao:
    def __init__(self):
        pass
    def criarNovoModulo(self, form):
        modulo = ModuloModel(idModulo=form.idModulo.data, numero=form.numero.data, nome=form.nome.data, idMundo=form.idMundo.data)
        bd.session.add(modulo)
        bd.session.commit()

    def getModulo(self,idModulo):
        modulo = ModuloModel.query.filter_by(idModulo=idModulo).first()
        if modulo:
            return modulo
        else:
            return None

    def carregarModulos(self):
        return ModuloModel.query.all()

    def carregarModuloPorId(self, idModulo):
        return ModuloModel.query.get(idModulo)

    def deletarModulo(self, idModulo):
        modulo = ModuloModel.query.get(idModulo)
        if modulo:
            bd.session.delete(modulo)
            bd.session.commit()

    def alterarModulo(self, form):
        idModulo = form.idModulo.data
        modulo_novo = ModuloModel(idModulo=idModulo, numero=form.numero.data, nome=form.nome.data, idMundo=form.idMundo.data)
        modulo_antigo = ModuloModel.query.get(idModulo)
        if modulo_antigo:
            modulo_antigo.numero = modulo_novo.numero
            modulo_antigo.nome = modulo_novo.nome
            modulo_antigo.idMundo = modulo_novo.idMundo
            bd.session.commit()

    def maiorIdModulo(self):
        maior = bd.session.query(bd.func.max(ModuloModel.idModulo)).scalar()
        if maior is None:
            return 1
        else:
            return maior + 1

    def moduloExiste(self, nome):
        modulo = ModuloModel.query.filter_by(nome=nome).first()
        return True if modulo else False