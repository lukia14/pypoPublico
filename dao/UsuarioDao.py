from flask import flash, session
from models.UsuarioModel import UsuarioModel
from models.ItemModel import ItemModel
from models.ProgressoModel import ProgressoModel
from models.EstoqueModel import EstoqueModel
from dao.ProgressoDao import ProgressoDao
from database import bd

class UsuarioDao:
    def __init__(self):
        pass

    def getUsuario(self,form):
        usuario = UsuarioModel.query.filter_by(nickname=form.nickname.data).first()
        return usuario
    
    def getPontuacao(self,idUsuario):
        usuario = UsuarioModel.query.filter_by(idUsuario=idUsuario).first()
        return usuario.pontuacao
    

    def getUsuarioPorNickname(self, nickname):
        usuario = UsuarioModel.query.filter_by(nickname=nickname).first()
        return usuario

    def getUsuarioPorId(self, idUsuario):
        usuario = UsuarioModel.query.filter_by(idUsuario=idUsuario).first()
        return usuario

    def setPontuacao(self,idUsuario,pontuacao):
        usuario = UsuarioModel.query.filter_by(idUsuario=idUsuario).first()
        usuario.pontuacao = pontuacao
        bd.session.commit()

    def criarNovoUsuario(self,form):
        oProgressoDao = ProgressoDao()
        novoUsuario = UsuarioModel.modeloUsuario(form)
        novoUsuario.pontuacao = 100
        bd.session.add(novoUsuario)
        bd.session.flush()
        idUsuario = novoUsuario.idUsuario

        oProgressoDao.criarProgresso(idUsuario)
        bd.session.commit()
        flash('Usuário cadastrado com sucesso!', 'success')
        session['usuario_logado'] = novoUsuario.idUsuario

    def autenticarUsuario(self,usuario):
        usuario = UsuarioModel.query.filter_by(nickname = usuario.nickname).first()
        if usuario:
            if usuario.senha == usuario.senha:
                session['usuario_logado'] = usuario.idUsuario
                flash('Usuário autenticado com sucesso!', 'success')
                return '/'
            else:
                flash('Erro ao autenticar. Verifique os dados e tente novamente.', 'error')
        else:
            flash('Usuário não encontrado. Verifique os dados e tente novamente.', 'error')
            return 'login'

    def alterarPerfil(self,form):
        usuarioAntigo = UsuarioModel.query.filter_by(idUsuario=session['usuario_logado']).first()
        email = form.email.data
        if usuarioAntigo:
            if not self.emailExiste(email):
                usuarioAntigo.email = form.email.data
                bd.session.commit()
                flash('Perfil atualizado com sucesso!', 'success')
                return True
            else:
                flash('Email já cadastrado','danger')
                return False
        else:
            flash('Usuário não encontrado. Verifique os dados e tente novamente.', 'error')
            return False
        
    def alterarSenha(self,form):
        usuarioAntigo = UsuarioModel.query.filter_by(idUsuario=session['usuario_logado']).first()
        senhaAntiga = usuarioAntigo.senha if usuarioAntigo else None
        if not senhaAntiga:
            flash('Usuário não encontrado. Verifique os dados e tente novamente.', 'error')

        if senhaAntiga != form.senhaAntiga.data:
            flash('Senha antiga incorreta. Verifique os dados e tente novamente.', 'error')

        if form.novaSenha.data != form.confirmarSenha.data:
            flash('As novas senhas não coincidem. Verifique os dados e tente novamente.', 'error')
            
        flash('Senha alterada com sucesso!', 'success')
        usuarioAntigo.senha = form.novaSenha.data
        bd.session.commit()
        
    def deletarConta(self, idUsuario):
        usuario = UsuarioModel.query.filter_by(idUsuario=idUsuario).first()
        if usuario:
            progresso = ProgressoModel.query.filter_by(idUsuario=idUsuario).first()
            estoque = EstoqueModel.query.filter_by(idUsuario=idUsuario).first()
            if estoque:
                bd.session.delete(estoque)
            if progresso:
                bd.session.delete(progresso)
            bd.session.delete(usuario)
            bd.session.commit()
            flash('Conta deletada com sucesso!', 'success')

    #funções de auxilio
    
    def UsuarioExiste(self,form):
        usuario = UsuarioModel.query.filter_by(nickname=form.nickname.data).first()
        if usuario:
            return True
        return False
    
    def emailExiste(self,email):
        usuario = UsuarioModel.query.filter_by(email=email).first()
        if usuario:
            return True
        return False