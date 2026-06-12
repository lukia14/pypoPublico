from flask import redirect, session, flash, url_for, request
from dao.MundoDao import MundoDao
from views.MundoView import MundoView
from helpers import FormularioMundo

class MundoService:
    def __init__(self):
        pass

    def listarMundos(self):
        oMundoDao = MundoDao()
        oMundoView = MundoView()
        lista = oMundoDao.carregarMundos()
        return oMundoView.listarMundos(lista)

    def cadastrarMundo(self):
        oMundoDao = MundoDao()
        oMundoView = MundoView()
        idMundo = oMundoDao.maiorIdMundo()
        form = FormularioMundo(idMundo=idMundo)
        return oMundoView.cadastrarMundo(form, aoEnviar='criarMundo')

    def criarMundo(self):
        oMundoDao = MundoDao()
        oMundoView = MundoView()
        form = FormularioMundo(request.form)
        if not form.validate_on_submit():
            flash('Erro ao criar mundo. Verifique os dados e tente novamente.','error')
            return redirect(oMundoView.cadastrarMundo(FormularioMundo(idMundo=oMundoDao.maiorIdMundo())))
        if oMundoDao.mundoExiste(form.linguagem.data):
            flash('Mundo já existe','error')
            return redirect(oMundoView.cadastrarMundo(FormularioMundo(idMundo=oMundoDao.maiorIdMundo())))
        oMundoDao.criarNovoMundo(form)
        flash('Mundo criado com sucesso!','success')
        return redirect(url_for('listarMundos'))

    def deletarMundo(self, idMundo):
        oMundoDao = MundoDao()
        oMundoView = MundoView()
        oMundoDao.deletarMundo(idMundo)
        flash('Mundo deletado com sucesso!', 'success')
        lista = oMundoDao.carregarMundos()
        return oMundoView.listarMundos(lista)

    def editarMundo(self, idMundo):
        oMundoDao = MundoDao()
        oMundoView = MundoView()
        mundo = oMundoDao.carregarMundoPorId(idMundo)
        form = FormularioMundo(obj=mundo)
        return oMundoView.editarMundo(form)

    def alterarMundo(self):
        oMundoDao = MundoDao()
        oMundoView = MundoView()
        form = FormularioMundo(request.form)
        if not form.validate_on_submit():
            flash('Erro ao alterar mundo. Verifique os dados e tente novamente.','error')
            return oMundoView.cadastrarMundo(FormularioMundo(idMundo=oMundoDao.maiorIdMundo()))
        oMundoDao.alterarMundo(form)
        flash('Mundo alterado com sucesso!','success')
        lista = oMundoDao.carregarMundos()
        return oMundoView.listarMundos(lista)
