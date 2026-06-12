from flask import render_template,request
from helpers import FormularioExercicio
class ExercicioView:
    def __init__(self):
        pass
    def cadastrarExercicio(self, idExercicio):
        form = FormularioExercicio(idExercicio=idExercicio)
        return render_template('formularioExercicio.html', form=form, titulo='Criar Exercício', aoEnviar='criarExercicio')
    
    def listarExercicios(self, listaExercicios):
        return render_template('listarExercicios.html', listaExercicios=listaExercicios, titulo='Lista de Exercícios')
    
    def editarExercicio(self,form):
        return render_template('formularioExercicio.html', form=form, titulo='Editar Exercício', aoEnviar='alterarExercicio')