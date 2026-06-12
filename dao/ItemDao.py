from models.ItemModel import ItemModel
from flask import jsonify
class ItemDao:
    def __init__(self):
        pass
    def criarNovoItem(self, form):
        item = ItemModel(idItem=form.idItem.data, nome=form.nome.data, descricao=form.descricao.data, valor=form.valor.data)
        from database import bd
        bd.session.add(item)
        bd.session.commit()

    def carregarItensLoja(self):
        listaItens = ItemModel.query.all()
        return listaItens

    def carregarItemPorId(self, idItem):
        return ItemModel.query.get(idItem)

    def deletarItem(self, idItem):
        from database import bd
        item = ItemModel.query.get(idItem)
        if item:
            bd.session.delete(item)
            bd.session.commit()

    def alterarItem(self, form):
        idItem = form.idItem.data
        item_novo = ItemModel(idItem=idItem, nome=form.nome.data, descricao=form.descricao.data, valor=form.valor.data)
        item_antigo = ItemModel.query.get(idItem)
        if item_antigo:
            item_antigo.nome = item_novo.nome
            item_antigo.descricao = item_novo.descricao
            item_antigo.valor = item_novo.valor
            from database import bd
            bd.session.commit()

    def maiorIdItem(self):
        from database import bd
        maior = bd.session.query(bd.func.max(ItemModel.idItem)).scalar()
        if maior is None:
            return 1
        else:
            return maior + 1

    def itemExiste(self, nome):
        item = ItemModel.query.filter_by(nome=nome).first()
        return True if item else False