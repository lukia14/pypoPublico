from service.MundoService import MundoService

class MundoController:
    def __init__(self):
        pass

    def listarMundos(self):
        oMundoService = MundoService()
        return oMundoService.listarMundos()

    def cadastrarMundo(self):
        oMundoService = MundoService()
        return oMundoService.cadastrarMundo()

    def criarMundo(self):
        oMundoService = MundoService()
        return oMundoService.criarMundo()

    def editarMundo(self, idMundo):
        oMundoService = MundoService()
        return oMundoService.editarMundo(idMundo)

    def alterarMundo(self):
        oMundoService = MundoService()
        return oMundoService.alterarMundo()

    def deletarMundo(self, idMundo):
        oMundoService = MundoService()
        return oMundoService.deletarMundo(idMundo)
