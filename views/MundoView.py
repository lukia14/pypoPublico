from flask import render_template

class MundoView:
    def __init__(self):
        pass
    
    def listarMundos(self, listaMundos):
        return render_template('listarMundos.html', listaMundos=listaMundos)

    def cadastrarMundo(self, form, aoEnviar='criarMundo'):
        return render_template('formularioMundo.html', form=form, titulo='Criar Mundo', aoEnviar=aoEnviar)

    def editarMundo(self, form):
        return render_template('formularioMundo.html', form=form, titulo='Editar Mundo', aoEnviar='alterarMundo')
