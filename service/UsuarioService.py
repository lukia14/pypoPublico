from flask import flash, request, redirect, url_for, session,jsonify
from helpers import FormularioUsuario,FormularioAlterarSenha
from views.UsuarioView import UsuarioView
from dao.UsuarioDao import UsuarioDao
from dao.ProgressoDao import ProgressoDao
class UsuarioService:
    def __init__(self):
        pass

    def cadastrar(self):
        oUsuarioView = UsuarioView()
        if self.verificarLogin():
            flash('Você já está logado.', 'danger')
            return oUsuarioView.index()
        
        return  oUsuarioView.cadastrar()

    def criarUsuario(self):        
        oUsuarioView = UsuarioView()
        oUsuarioDao = UsuarioDao()
        form = FormularioUsuario(request.form)
        if not form.validate_on_submit():
            flash('Erro ao cadastrar usuário. Verifique os dados e tente novamente.','danger')
            return redirect(url_for('cadastrar'))
        
        if oUsuarioDao.UsuarioExiste(form):
            flash('Usuario já cadastrado','danger')
            return redirect(url_for('login'))
        else:
            oUsuarioDao.criarNovoUsuario(form)
        return oUsuarioView.principal()
    
    def login(self):
        form = FormularioUsuario()
        oUsuarioView = UsuarioView()
        if self.verificarLogin():
            oUsuarioDao = UsuarioDao()
            usuario = oUsuarioDao.getUsuarioPorId(session['usuario_logado'])
            nome = usuario.nickname if usuario else session['usuario_logado']
            flash(f'Você já está logado como {nome}','danger')
            return oUsuarioView.principal()
       
        return oUsuarioView.login(form)
    
    def autenticar(self):
        oUsuarioView = UsuarioView()
        oUsuarioDao = UsuarioDao()
        form = FormularioUsuario(request.form)
        usuario = oUsuarioDao.getUsuario(form)
        if usuario:
            if usuario.senha == form.senha.data and usuario.email == form.email.data:
                session['usuario_logado'] = usuario.idUsuario
                flash('Usuário autenticado com sucesso!', 'success')
                return oUsuarioView.principal()
            
        flash('Erro ao autenticar. Verifique os dados e tente novamente.', 'danger')
        return oUsuarioView.login(form)

    def logout(self):
        session['usuario_logado'] = None   
        flash('Você foi desconectado com sucesso!', 'success')
        return redirect(url_for('index'))
    
    def principal(self):
        oUsuarioView = UsuarioView()
        if not self.verificarLogin():
            flash('Faça login para acessar a página principal', 'danger')
            return redirect(url_for('login'))
        
        return oUsuarioView.principal()
    
    def configuracoes(self):
        oUsuarioView = UsuarioView()
        oUsuarioDao = UsuarioDao()
        if not self.verificarLogin():
            flash('Faça login para acessar as configurações', 'danger')
            return redirect(url_for('login'))
        
        usuario = oUsuarioDao.getUsuarioPorId(session['usuario_logado'])
        return oUsuarioView.configuracoes(usuario)
    
    def apiSalvarPontuacao(self):
        idUsuario = session['usuario_logado']
        oUsuarioDao = UsuarioDao()
        oProgressoDao = ProgressoDao()
        dados = request.get_json(silent=True)
        if not dados:
            return jsonify({'status': 'erro', 'mensagem': 'Dados não recebidos'}), 400
        pontuacao = dados.get('pontuacao')
        idFase = dados.get('idFase')
        oUsuarioDao.setPontuacao(idUsuario,pontuacao)
        oProgressoDao.setProgresso(idUsuario,idFase)

        return jsonify({"status": "sucesso", "mensagem": "Pontuação salva com sucesso!"}), 200
    
    def alterarPerfil(self):
        oUsuarioDao = UsuarioDao()
        form = FormularioUsuario(request.form)
        if not self.verificarLogin():
            flash('Faça login para alterar o perfil', 'danger')
            return redirect(url_for('login'))
        oUsuarioDao.alterarPerfil(form)
        return redirect(url_for('configuracoes'))
    
    def alterarSenha(self):
        oUsuarioDao = UsuarioDao()
        oUsuarioView = UsuarioView()
        form = FormularioAlterarSenha(request.form)
        if not self.verificarLogin():
            flash('Faça login para alterar a senha', 'danger')
            return redirect(url_for('login'))
        oUsuarioDao.alterarSenha(form)
        return oUsuarioView.configuracoes(oUsuarioDao.getUsuarioPorId(session['usuario_logado']))
        
    def deletarConta(self):
        oUsuarioDao = UsuarioDao()
        if not self.verificarLogin():
            flash('Faça login para deletar a conta', 'danger')
            return redirect(url_for('login'))
        
        oUsuarioDao.deletarConta(session['usuario_logado'])
        session['usuario_logado'] = None
        flash('Conta deletada com sucesso!', 'success')
        return redirect(url_for('principal'))
    
    #funções auxiliares
    def verificarLogin(self):
        if 'usuario_logado' not in session or session['usuario_logado'] is None:
            flash('Faça login para acessar esta página', 'danger')
            return False
        return True