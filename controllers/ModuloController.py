from service.ModuloService import ModuloService

class ModuloController:
    def __init__(self):
        pass

    def modulo(self):
        oModuloService = ModuloService()
        return oModuloService.modulo()
    
    def listarModulos(self):
        oModuloService = ModuloService()
        return oModuloService.listarModulos()

    def cadastrarModulo(self):
        oModuloService = ModuloService()
        return oModuloService.cadastrarModulo()

    def criarModulo(self):
        oModuloService = ModuloService()
        return oModuloService.criarModulo()

    def editarModulo(self, idModulo):
        oModuloService = ModuloService()
        return oModuloService.editarModulo(idModulo)

    def alterarModulo(self):
        oModuloService = ModuloService()
        return oModuloService.alterarModulo()

    def deletarModulo(self, idModulo):
        oModuloService = ModuloService()
        return oModuloService.deletarModulo(idModulo)