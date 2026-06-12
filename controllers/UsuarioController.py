from service.UsuarioService import UsuarioService
from views.UsuarioView import UsuarioView
class UsuarioController:
    def __init__(self):
        pass


    def index(self):
        oUsuarioView = UsuarioView()
        return  oUsuarioView.index()

    def cadastrar(self):
        oUsuarioService = UsuarioService()
        return  oUsuarioService.cadastrar()
    
    def criar(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.criarUsuario()
    
    def login(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.login()

    def autenticar(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.autenticar()

    def logout(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.logout()
    
    def principal(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.principal()
    
    def configuracoes(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.configuracoes()
    
    def apiSalvarPontuacao(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.apiSalvarPontuacao()
    
    def alterarPerfil(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.alterarPerfil()
    
    def alterarSenha(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.alterarSenha()
    
    def deletarConta(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.deletarConta()
    
    

    