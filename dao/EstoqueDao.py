from models.EstoqueModel import EstoqueModel
from models.ItemModel import ItemModel
from database import bd

class Estoquedao:
    def __init__(self):
        pass

    def carregarEstoqueUsuario(self, idUsuario):
       
       return bd.session.query(ItemModel.nome, EstoqueModel.qtd).join(EstoqueModel, ItemModel.idItem == EstoqueModel.idItem).filter(EstoqueModel.idUsuario == idUsuario).all()
    
    def carregarEstoqueUsuarioAPI(self, idUsuario):
        return bd.session.query(ItemModel.idItem, ItemModel.nome, ItemModel.descricao, ItemModel.valor, EstoqueModel.qtd).join(EstoqueModel, ItemModel.idItem == EstoqueModel.idItem).filter(EstoqueModel.idUsuario == idUsuario).all()
    
    def adicionarAoEstoque(self,idUsuario,idItem,qtd):
        estoqueAntigo = EstoqueModel.query.filter_by(idUsuario=idUsuario,idItem=idItem).first()
        if estoqueAntigo:
            estoqueAntigo.qtd = qtd
        else:
            estoque = EstoqueModel(
            qtd = qtd,
            idUsuario = idUsuario, 
            idItem = idItem
            )
            bd.session.add(estoque)
        bd.session.commit()