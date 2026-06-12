from flask import redirect, session, flash, url_for
from app import app
from dao.UsuarioDao import UsuarioDao
from dao.ProgressoDao import ProgressoDao
from dao.FaseDao import FaseDao
from helpers import FormularioExercicio, FormularioFase
from views.FaseView import FaseView

class FaseService:
    def __init__(self):
        pass
    def fase(self,idFase):
        idUsuario = session['usuario_logado']
        oFaseView = FaseView()
        oProgressoDao = ProgressoDao()
        oFaseDao = FaseDao()
        if not self.verificarLogin():
            flash('Você precisa estar logado para acessar essa página.', 'error')
            return redirect(url_for('login', proxima=url_for('fase')))
        else:
            progresso = oProgressoDao.getProgresso(idUsuario)
            if idFase > progresso.idFase:
                flash(f'Fase ainda não desbloqueada. Fase atual: {progresso.idFase+1}')
                return redirect(url_for('modulo'))
            fase = oFaseDao.getFase(idFase)
            lista_exercicios = fase.exercicio

            lista_dicionarios = self.criar_lista_exercicios_dict(lista_exercicios)# Converte a lista de exercícios em uma lista de dicionários
            return oFaseView.fase(idUsuario,lista_dicionarios, fase.idFase)
        
    def material(self,idFase):
        idUsuario = session['usuario_logado']
        oFaseView = FaseView()
        oProgressoDao = ProgressoDao()
        oFaseDao = FaseDao()
        if not self.verificarLogin():
            flash('Você precisa estar logado para acessar essa página.', 'error')
            return redirect(url_for('login', proxima=url_for('fase')))
        else:
            progresso = oProgressoDao.getProgresso(idUsuario)
            if idFase > progresso.idFase:
                flash(f'Fase ainda não desbloqueada. Fase atual: {progresso.idFase+1}')
                return redirect(url_for('modulo'))
            fase = oFaseDao.getFase(idFase)
            return oFaseView.material(fase)
            
        
    #funções auxiliares
    def criar_lista_exercicios_dict(self,lista_exercicios):
        lista_dicionarios = []
        for exercicio in lista_exercicios:
            dict_exercicio = {
                'idExercicio': exercicio.idExercicio,
                'titulo': exercicio.titulo,
                'enunciado': exercicio.enunciado,
                'alternativaA': exercicio.alternativaA,
                'alternativaB': exercicio.alternativaB,
                'alternativaC': exercicio.alternativaC,
                'alternativaD': exercicio.alternativaD,
                'resposta': exercicio.resposta
            }
            lista_dicionarios.append(dict_exercicio)
        return lista_dicionarios
    
    def listarFases(self):
        oFaseDao = FaseDao()
        oFaseView = FaseView()
        listaFases = oFaseDao.getListaFases()
        return oFaseView.listarFases(listaFases)
    
    def cadastrarFase(self):
        oFaseView = FaseView()
        oFaseDao = FaseDao()
        idFase = oFaseDao.maiorIdFase()
        form = FormularioFase(idFase=idFase)
        return oFaseView.cadastrarFase(form, aoEnviar='criarFase')

    def criarFase(self):
        from flask import request, redirect, flash, url_for
        oFaseDao = FaseDao()
        oFaseView = FaseView()
        form = FormularioFase(request.form)
        if not form.validate_on_submit():
            flash('Erro ao criar fase. Verifique os dados e tente novamente.','error')
            return redirect(oFaseView.cadastrarFase(FormularioFase(idFase=oFaseDao.maiorIdFase())))
        if oFaseDao.faseExiste(form.materialApoio.data):
            flash('Fase já existe','error')
            return redirect(oFaseView.cadastrarFase(FormularioFase(idFase=oFaseDao.maiorIdFase())))
        oFaseDao.criarNovaFase(form)
        flash('Fase criada com sucesso!','success')
        return redirect(url_for('listarFases'))

    def deletarFase(self, idFase):
        from flask import flash
        oFaseDao = FaseDao()
        oFaseView = FaseView()
        oFaseDao.deletarFase(idFase)
        flash('Fase deletada com sucesso!', 'success')
        listaFases = oFaseDao.getListaFases()
        return oFaseView.listarFases(listaFases)

    def editarFase(self, idFase):
        from helpers import FormularioFase
        oFaseDao = FaseDao()
        oFaseView = FaseView()
        fase = oFaseDao.carregarFasePorId(idFase)
        form = FormularioFase(obj=fase)
        return oFaseView.editarFase(form)

    def alterarFase(self):
        from flask import request, flash, redirect
        oFaseDao = FaseDao()
        oFaseView = FaseView()
        form = FormularioFase(request.form)
        if not form.validate_on_submit():
            flash('Erro ao alterar fase. Verifique os dados e tente novamente.','error')
            return oFaseView.cadastrarFase(FormularioFase(idFase=oFaseDao.maiorIdFase()))
        oFaseDao.alterarFase(form)
        flash('Fase alterada com sucesso!','success')
        listaFases = oFaseDao.getListaFases()
        return oFaseView.listarFases(listaFases)

    
    #funções auxiliares
    def verificarLogin(self):
        if 'usuario_logado' not in session or session['usuario_logado'] is None:
            flash('Faça login para acessar esta página', 'danger')
            return False
        return True