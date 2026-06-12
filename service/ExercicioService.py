from flask import render_template, request, redirect, session, flash, url_for
from helpers import FormularioExercicio
from views.ExercicioView import ExercicioView
from dao.ExercicioDao import ExercicioDao
from models.ExercicioModel import ExercicioModel

class ExercicioService:
    def __init__(self):
        pass

    def cadastrarExercicio(self):
        oExercicioDao = ExercicioDao()
        oExercicioView = ExercicioView()
        idExercicio = oExercicioDao.maiorIdExercicio()
        return oExercicioView.cadastrarExercicio(idExercicio)
        
    
    def criarExercicio(self):
        oExercicioView = ExercicioView()
        oExercicioDao = ExercicioDao()
        oExercicioModel = ExercicioModel()
        form = FormularioExercicio(request.form)
        if not form.validate_on_submit():
            flash('Erro ao criar exercício. Verifique os dados e tente novamente.','error')
            return redirect(oExercicioView.cadastrarExercicio())
        if oExercicioDao.exercicioExiste(form.enunciado.data):
            return redirect(oExercicioView.cadastrarExercicio())
        else:
            oExercicioDao.criarNovoExercicio(form)
        
        flash('Exercício criado com sucesso!', 'success')
        return redirect(url_for('listarExercicios')) 
    
    def listarExercicios(self):
        oExercicioDao = ExercicioDao()
        exercicios = oExercicioDao.carregarExercicios()
        oExercicioView = ExercicioView()
        return oExercicioView.listarExercicios(exercicios)
    
    def deletarExercicio(self, idExercicio):
        oExercicioDao = ExercicioDao()
        oExercicioView = ExercicioView()
        oExercicioDao.deletarExercicio(idExercicio)
        flash('Exercício deletado com sucesso!', 'success')
        exercicios = oExercicioDao.carregarExercicios()
        return oExercicioView.listarExercicios(exercicios)

    def editarExercicio(self, idExercicio):
        oExercicioDao = ExercicioDao()
        oExercicioView = ExercicioView()
        exercicio = oExercicioDao.carregarExercicioPorId(idExercicio)
        form = FormularioExercicio(obj=exercicio)
        return oExercicioView.editarExercicio(form)
    
    def alterarExercicio(self):
        oExercicioDao = ExercicioDao()
        oExercicioView = ExercicioView()
        form = FormularioExercicio(request.form)
        if not form.validate_on_submit():
            flash('Erro ao alterar exercício. Verifique os dados e tente novamente.','error')
            return oExercicioView.cadastrarExercicio(oExercicioDao.maiorIdExercicio())
        
        oExercicioDao.alterarExercicio(form)
        flash('Exercício alterado com sucesso!', 'success')
        exercicios = oExercicioDao.carregarExercicios()
        return oExercicioView.listarExercicios(exercicios)
    
