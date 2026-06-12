from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, IntegerField,TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange

class FormularioUsuario(FlaskForm):
    nickname = StringField("Nickname", validators=[DataRequired(), Length(min=1, max=20)])
    email = StringField('Email', validators=[DataRequired(), Length(min=1, max=35)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=1, max=35)])
    enviar = SubmitField('Enviar')
class FormularioAlterarSenha(FlaskForm):
    senhaAntiga = PasswordField('Senha Antiga', validators=[DataRequired(), Length(min=1, max=35)])
    novaSenha = PasswordField('Nova Senha', validators=[DataRequired(), Length(min=1, max=35)])
    confirmarSenha = PasswordField('Confirmar Nova Senha', validators=[DataRequired(), Length(min=1, max=35), validators.EqualTo('novaSenha', message='As senhas devem coincidir')])
    enviar = SubmitField('Alterar Senha')

class FormularioExercicio(FlaskForm):
    idExercicio = IntegerField("Id do Exercício", validators=[DataRequired()],render_kw={'readonly': True})
    numero = IntegerField("Número do Exercício", validators=[DataRequired()])
    idFase = IntegerField("Id da Fase", validators=[DataRequired()])
    titulo = StringField("Título", validators=[DataRequired(), Length(min=1, max=35)])
    enunciado = StringField("Enunciado", validators=[DataRequired()])
    alternativaA = StringField("Alternativa A", validators=[DataRequired(), Length(min=1, max=99)])
    alternativaB = StringField("Alternatica B", validators=[DataRequired(), Length(min = 1, max=99)])
    alternativaC = StringField("Alternativa C", validators=[DataRequired(),Length(min=1, max=99)])
    alternativaD = StringField("ALternativa D", validators=[DataRequired(), Length(min=1, max=99)])
    resposta = StringField("Alternativa da Resposta",validators=[DataRequired()])
    
    enviar = SubmitField("Criar Exercício")

class FormularioFase(FlaskForm):
    idFase = IntegerField("Id da Fase",validators=[DataRequired()])
    titulo= StringField("Titulo da Fase",validators=[DataRequired()])
    materialApoio = TextAreaField("Material de apoio",validators=[DataRequired()])
    idModulo = StringField("Id do módulo",validators=[DataRequired()])
    enviar = SubmitField("Enviar")


class FormularioItem(FlaskForm):
    idItem = IntegerField("Id do Item", validators= [DataRequired()])
    nome = StringField("Nome do Item", validators=[DataRequired(), Length(min=1, max = 30)])
    descricao = StringField("Descrição", validators=[DataRequired(), Length(min=1, max=99)])
    valor = IntegerField("Valor do Item", validators=[DataRequired()])

    enviar = SubmitField("Criar Item")

class FormularioModulo(FlaskForm):
    idModulo = IntegerField("Id do Módulo", validators=[DataRequired()])
    numero = IntegerField("Número do Módulo", validators=[DataRequired()])
    nome = StringField("Nome", validators=[DataRequired(), Length(min=1, max=35)])
    idMundo = IntegerField("Id do Mundo", validators=[DataRequired()])
    enviar = SubmitField("Criar Módulo")

class FormularioMundo(FlaskForm):
    idMundo = IntegerField("Id do Mundo", validators=[DataRequired()])
    linguagem = StringField("Linguagem", validators=[DataRequired(), Length(min=1, max=20)])
    enviar = SubmitField("Criar Mundo")

