from app import app
from controllers.ExercicioController import ExercicioController
from controllers.FaseController import FaseController
from controllers.ModuloController import ModuloController
from controllers.ItemController import ItemController
from controllers.MundoController import MundoController
@app.route('/modulo')
def modulo():
    oModuloController = ModuloController()
    return oModuloController.modulo()

@app.route('/fase/<int:idFase>')
def fase(idFase):
    oFaseController = FaseController()
    return oFaseController.fase(idFase)

@app.route('/material/<int:idFase>')
def material(idFase):
    oFaseController = FaseController()
    return oFaseController.material(idFase)

@app.route('/conclusaoFase/<int:idFase>/<int:pontuacao>')
def conclusaoFase(idFase,pontuacao):
    oFaseController = FaseController()
    return oFaseController.conclusaoFase(idFase=idFase,pontuacao=pontuacao)

# Exercicio
@app.route('/cadastrarExercicio')
def cadastrarExercicio():
    oExercicioController = ExercicioController()
    return oExercicioController.cadastrarExercicio()


@app.route('/criarExercicio', methods=['POST'])
def criarExercicio():
    oExercicioController = ExercicioController()
    return oExercicioController.criarExercicio()
@app.route('/listarExercicios')
def listarExercicios():
    oExercicioController = ExercicioController()
    return oExercicioController.listarExercicios()

@app.route('/exercicio/editar/<int:idExercicio>')
def editarExercicio(idExercicio):
    oExercicioController = ExercicioController()
    return oExercicioController.editarExercicio(idExercicio)

@app.route('/exercicio/alterar',methods=['POST'])
def alterarExercicio():
    oExercicioController = ExercicioController()
    return oExercicioController.alterarExercicio()

@app.route('/exercicio/deletar/<int:idExercicio>')
def deletarExercicio(idExercicio):
    oExercicioController = ExercicioController()
    return oExercicioController.deletarExercicio(idExercicio)

#Fase
@app.route('/listarFases')
def listarFases():
    oFaseController = FaseController()
    return oFaseController.listarFases()

@app.route('/cadastrarFase')
def cadastrarFase():
    oFaseController = FaseController()
    return oFaseController.cadastrarFase()

@app.route('/criarFase', methods=['POST'])
def criarFase():
    oFaseController = FaseController()
    return oFaseController.criarFase()

@app.route('/fase/editar/<int:idFase>')
def editarFase(idFase):
    oFaseController = FaseController()
    return oFaseController.editarFase(idFase)

@app.route('/fase/alterar', methods=['POST'])
def alterarFase():
    oFaseController = FaseController()
    return oFaseController.alterarFase()

@app.route('/fase/deletar/<int:idFase>')
def deletarFase(idFase):
    oFaseController = FaseController()
    return oFaseController.deletarFase(idFase)
#Modulo
@app.route('/listarModulos')
def listarModulos():
    oModuloController = ModuloController()
    return oModuloController.listarModulos()

@app.route('/cadastrarModulo')
def cadastrarModulo():
    oModuloController = ModuloController()
    return oModuloController.cadastrarModulo()

@app.route('/criarModulo', methods=['POST'])
def criarModulo():
    oModuloController = ModuloController()
    return oModuloController.criarModulo()

@app.route('/modulo/editar/<int:idModulo>')
def editarModulo(idModulo):
    oModuloController = ModuloController()
    return oModuloController.editarModulo(idModulo)

@app.route('/modulo/alterar', methods=['POST'])
def alterarModulo():
    oModuloController = ModuloController()
    return oModuloController.alterarModulo()

@app.route('/modulo/deletar/<int:idModulo>')
def deletarModulo(idModulo):
    oModuloController = ModuloController()
    return oModuloController.deletarModulo(idModulo)

#Mundo
@app.route('/listarMundos')
def listarMundos():
    oMundoController = MundoController()
    return oMundoController.listarMundos()

@app.route('/cadastrarMundo')
def cadastrarMundo():
    oMundoController = MundoController()
    return oMundoController.cadastrarMundo()

@app.route('/criarMundo', methods=['POST'])
def criarMundo():
    oMundoController = MundoController()
    return oMundoController.criarMundo()

@app.route('/mundo/editar/<int:idMundo>')
def editarMundo(idMundo):
    oMundoController = MundoController()
    return oMundoController.editarMundo(idMundo)

@app.route('/mundo/alterar', methods=['POST'])
def alterarMundo():
    oMundoController = MundoController()
    return oMundoController.alterarMundo()

@app.route('/mundo/deletar/<int:idMundo>')
def deletarMundo(idMundo):
    oMundoController = MundoController()
    return oMundoController.deletarMundo(idMundo)

#Itens
@app.route('/listarItens')
def listarItens():
    oItemController = ItemController()
    return oItemController.listarItens()

@app.route('/cadastrarItem')
def cadastrarItem():
    oItemController = ItemController()
    return oItemController.cadastrarItem()

@app.route('/criarItem', methods=['POST'])
def criarItem():
    oItemController = ItemController()
    return oItemController.criarItem()

@app.route('/item/editar/<int:idItem>')
def editarItem(idItem):
    oItemController = ItemController()
    return oItemController.editarItem(idItem)

@app.route('/item/alterar', methods=['POST'])
def alterarItem():
    oItemController = ItemController()
    return oItemController.alterarItem()

@app.route('/item/deletar/<int:idItem>')
def deletarItem(idItem):
    oItemController = ItemController()
    return oItemController.deletarItem(idItem)