from flask import redirect, session, flash, url_for
from dao.ModuloDao import ModuloDao
from dao.FaseDao import FaseDao
from dao.ProgressoDao import ProgressoDao
from views.ModuloView import ModuloView
class ModuloService:
    def __init__(self):
        pass

    def modulo(self):
        if not self.verificarLogin():
            return redirect('login')
        idUsuario = session['usuario_logado']
        oModuloDao = ModuloDao()
        oModuloView = ModuloView()
        oFaseDao = FaseDao()
        oProgressoDao = ProgressoDao()
        progresso = oProgressoDao.getProgresso(idUsuario)
        if progresso:
            idFase = progresso.idFase
        else:
            idFase = 1
        idModulo = oFaseDao.getFase(idFase).idModulo
        listaFases = oModuloDao.getModulo(idModulo).fase
        if listaFases:
            return oModuloView.modulo(listaFases)
        else:
            flash('Módulo não encontrado','danger')
            return redirect('/principal')
    
    def listarModulos(self):
        from dao.ModuloDao import ModuloDao
        oModuloDao = ModuloDao()
        oModuloView = ModuloView()
        lista = oModuloDao.carregarModulos()
        return oModuloView.listarModulos(lista)

    def cadastrarModulo(self):
        from helpers import FormularioModulo
        oModuloDao = ModuloDao()
        oModuloView = ModuloView()
        idModulo = oModuloDao.maiorIdModulo()
        form = FormularioModulo(idModulo=idModulo)
        return oModuloView.cadastrarModulo(form, aoEnviar='criarModulo')

    def criarModulo(self):
        from flask import request, redirect, flash, url_for
        from dao.ModuloDao import ModuloDao
        from helpers import FormularioModulo
        oModuloDao = ModuloDao()
        oModuloView = ModuloView()
        form = FormularioModulo(request.form)
        if not form.validate_on_submit():
            flash('Erro ao criar módulo. Verifique os dados e tente novamente.','error')
            return redirect(oModuloView.cadastrarModulo(FormularioModulo(idModulo=oModuloDao.maiorIdModulo())))
        if oModuloDao.moduloExiste(form.nome.data):
            flash('Módulo já existe','error')
            return redirect(oModuloView.cadastrarModulo(FormularioModulo(idModulo=oModuloDao.maiorIdModulo())))
        oModuloDao.criarNovoModulo(form)
        flash('Módulo criado com sucesso!','success')
        return redirect(url_for('listarModulos'))

    def deletarModulo(self, idModulo):
        from flask import flash
        oModuloDao = ModuloDao()
        oModuloView = ModuloView()
        oModuloDao.deletarModulo(idModulo)
        flash('Módulo deletado com sucesso!', 'success')
        lista = oModuloDao.carregarModulos()
        return oModuloView.listarModulos(lista)

    def editarModulo(self, idModulo):
        from helpers import FormularioModulo
        oModuloDao = ModuloDao()
        oModuloView = ModuloView()
        modulo = oModuloDao.carregarModuloPorId(idModulo)
        form = FormularioModulo(obj=modulo)
        return oModuloView.editarModulo(form)

    def alterarModulo(self):
        from flask import request, flash
        from helpers import FormularioModulo
        oModuloDao = ModuloDao()
        oModuloView = ModuloView()
        form = FormularioModulo(request.form)
        if not form.validate_on_submit():
            flash('Erro ao alterar módulo. Verifique os dados e tente novamente.','error')
            return oModuloView.cadastrarModulo(FormularioModulo(idModulo=oModuloDao.maiorIdModulo()))
        oModuloDao.alterarModulo(form)
        flash('Módulo alterado com sucesso!','success')
        lista = oModuloDao.carregarModulos()
        return oModuloView.listarModulos(lista)
        
                        
#funções auxiliares
    def verificarLogin(self):
        if 'usuario_logado' not in session or session['usuario_logado'] is None:
            flash('Faça login para acessar esta página', 'danger')
            return False
        return True