from app import app
from controllers.UsuarioController import UsuarioController

@app.route('/')
def index():
    oUsuarioController = UsuarioController()
    return  oUsuarioController.index()

@app.route('/cadastrar')
def cadastrar():
    oUsuarioController = UsuarioController()
    return  oUsuarioController.cadastrar()

@app.route('/criar', methods=['POST'])
def criar():
    oUsuarioController = UsuarioController()
    return oUsuarioController.criar()

@app.route('/login')
def login():
    oUsuarioController = UsuarioController()
    return oUsuarioController.login()
    

@app.route('/autenticar', methods=['POST'])
def autenticar():
    oUsuarioController = UsuarioController()
    return oUsuarioController.autenticar()

@app.route('/logout')
def logout():
    oUsuarioController = UsuarioController()
    return oUsuarioController.logout()

@app.route('/alterarSenha', methods=['POST'])
def alterarSenha():
    oUsuarioController = UsuarioController()
    return oUsuarioController.alterarSenha()

@app.route('/alterarPerfil', methods=['POST'])
def alterarPerfil():
    oUsuarioController = UsuarioController()
    return oUsuarioController.alterarPerfil()

@app.route('/deletarConta', methods=['POST'])
def deletarConta():
    oUsuarioController = UsuarioController()
    return oUsuarioController.deletarConta()





