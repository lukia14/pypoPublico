from flask import render_template,request
from helpers import FormularioUsuario, FormularioAlterarSenha

class UsuarioView:
    def __init__(self):
        pass
    
    def index(self):
        return render_template('index.html',titulo='PaginaInicial')
    
    def cadastrar(self):
        form = FormularioUsuario()
        return render_template('cadastrar.html', form=form, titulo='Cadastro')
    
    def login(self,form):
        proxima = request.args.get('proxima')
        return render_template('login.html', titulo='Login', form=form, proxima = proxima)
    
    def principal(self):
        return render_template('principal.html')
    
    def configuracoes(self, usuario):
        formPerfil = FormularioUsuario()
        formSenha = FormularioAlterarSenha()
        return render_template('configuracoes.html', usuario=usuario, formPerfil=formPerfil, formSenha=formSenha)

    
