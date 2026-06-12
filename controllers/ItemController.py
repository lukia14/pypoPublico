from service.ItemService import ItemService

class ItemController:
    def __init__(self):
        pass

    def loja(self):
        oItemService = ItemService()
        return oItemService.loja()

    def apiItensLoja(self):
        oItemService = ItemService()
        return oItemService.apiItensLoja()
    
    def apiEstoque(self):
        oItemService = ItemService()
        return oItemService.apiEstoque()
    
    def apiSalvarCompra(self):
        oItemService = ItemService()
        return oItemService.apiSalvarCompra()
    
    # Admin CRUD
    def listarItens(self):
        oItemService = ItemService()
        return oItemService.listarItens()

    def cadastrarItem(self):
        oItemService = ItemService()
        return oItemService.cadastrarItem()

    def criarItem(self):
        oItemService = ItemService()
        return oItemService.criarItem()

    def editarItem(self, idItem):
        oItemService = ItemService()
        return oItemService.editarItem(idItem)

    def alterarItem(self):
        oItemService = ItemService()
        return oItemService.alterarItem()

    def deletarItem(self, idItem):
        oItemService = ItemService()
        return oItemService.deletarItem(idItem)