from flask import render_template
class ModuloView:
    def __init__(self):
        pass

    def modulo(self,listaFases):
        return render_template('trilhaModulo.html',listaFases=listaFases)
    
    def listarModulos(self, listaModulos):
        return render_template('listarModulos.html', listaModulos=listaModulos)

    def cadastrarModulo(self, form, aoEnviar='criarModulo'):
        return render_template('formularioModulo.html', form=form, titulo='Criar Módulo', aoEnviar=aoEnviar)

    def editarModulo(self, form):
        return render_template('formularioModulo.html', form=form, titulo='Editar Módulo', aoEnviar='alterarModulo')