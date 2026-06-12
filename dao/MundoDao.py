from database import bd
from models.MundoModel import MundoModel
class MundoDao:
    def __init__(self):
        pass

    def criarNovoMundo(self, form):
        mundo = MundoModel(linguagem=form.linguagem.data, idMundo=form.idMundo.data)
        bd.session.add(mundo)
        bd.session.commit()

    def carregarMundos(self):
        return MundoModel.query.all()

    def carregarMundoPorId(self, idMundo):
        return MundoModel.query.get(idMundo)

    def deletarMundo(self, idMundo):
        mundo = MundoModel.query.get(idMundo)
        if mundo:
            bd.session.delete(mundo)
            bd.session.commit()

    def alterarMundo(self, form):
        idMundo = form.idMundo.data
        mundo_novo = MundoModel(linguagem=form.linguagem.data, idMundo=idMundo)
        mundo_antigo = MundoModel.query.get(idMundo)
        if mundo_antigo:
            mundo_antigo.linguagem = mundo_novo.linguagem
            bd.session.commit()

    def maiorIdMundo(self):
        maior = bd.session.query(bd.func.max(MundoModel.idMundo)).scalar()
        if maior is None:
            return 1
        else:
            return maior + 1

    def mundoExiste(self, linguagem):
        mundo = MundoModel.query.filter_by(linguagem=linguagem).first()
        return True if mundo else False
