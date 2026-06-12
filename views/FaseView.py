from flask import render_template, request

class FaseView:
    def __init__(self):
        pass
    
    def fase(self, usuario, lista_dicionarios, idFase):
        return render_template('fase.html', titulo='Fase 1', usuario=usuario, lista_exercicios=lista_dicionarios, idFase=idFase)
    
    def material(self,fase):
        return render_template('material.html',fase=fase)

    def conclusaoFase(self, pontuacao, idFase):
        return render_template('conclusaoFase.html', idFase=idFase, pontuacao=pontuacao)
    
    def listarFases(self,listaFases):
        return render_template('listarFases.html',listaFases=listaFases)
    
    def cadastrarFase(self, form, aoEnviar='criarFase'):
        return render_template('formularioFase.html', form=form, titulo='Criar Fase', aoEnviar=aoEnviar)

    def editarFase(self, form):
        return render_template('formularioFase.html', form=form, titulo='Editar Fase', aoEnviar='alterarFase')