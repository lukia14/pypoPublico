from flask import flash, redirect, session, url_for,jsonify,request
from views.ItemView import ItemView
from dao.EstoqueDao import Estoquedao
from dao.ItemDao import ItemDao
from dao.UsuarioDao import UsuarioDao
class ItemService:
    def __init__(self):
        pass

    def loja(self):
            idUsuario = session['usuario_logado']
            oItemDao = ItemDao()
            oEstoqueDao = Estoquedao()
            oUsuarioDao = UsuarioDao()
            pontuacao = oUsuarioDao.getPontuacao(idUsuario)
            if not self.verificarLogin():
                flash('Faça login para acessar a loja', 'danger')
                return redirect(url_for('login'))
            listaItens = oItemDao.carregarItensLoja()
            listaEstoque = oEstoqueDao.carregarEstoqueUsuario(idUsuario)              
            oItemView = ItemView()
            return oItemView.loja(listaItens, listaEstoque,pontuacao)

    def apiItensLoja(self):
        oItemDao = ItemDao()
        listaItens = oItemDao.carregarItensLoja()
        listaParaJS =[]
        for item in listaItens:
            listaParaJS.append({
                'idItem': item.idItem,
                'nome': item.nome,
                'descricao': item.descricao,
                'valor': item.valor
            })
        return jsonify(listaParaJS)
    
    def apiEstoque(self):
        oEstoqueDao = Estoquedao()
        listaEstoque = oEstoqueDao.carregarEstoqueUsuarioAPI(session['usuario_logado'])
        listaParaJS = []
        for item in listaEstoque:
            listaParaJS.append({
                'idItem': item.idItem,
                'nome': item.nome,
                'descricao': item.descricao,
                'valor': item.valor,
                'qtd': item.qtd  
            })
        return jsonify(listaParaJS)
    
    def apiSalvarCompra(self):
        oEstoqueDao = Estoquedao()
        oUsuarioDao = UsuarioDao()
        dados = request.get_json(silent=True)
        if not dados:
            return jsonify({'status': 'erro', 'mensagem': 'Dados de compra não fornecidos'}), 400
    
        listaEstoqueEnviada = dados.get('estoque')     
        novaPontuacao = dados.get('pontuacao')          
        oUsuarioDao.setPontuacao(session['usuario_logado'],novaPontuacao)
        if listaEstoqueEnviada:
            for item in listaEstoqueEnviada:
                idItem= item.get('idItem')
                qtd= item.get('qtd')
                oEstoqueDao.adicionarAoEstoque(session['usuario_logado'],idItem,qtd)
        return {"status": "sucesso", "mensagem": "Compra salva com sucesso!"}, 200
    
    #funções auxiliares
    def verificarLogin(self):
        if 'usuario_logado' not in session or session['usuario_logado'] is None:
            flash('Faça login para acessar esta página', 'danger')
            return False
        return True

    # Admin CRUD
    def listarItens(self):
        oItemDao = ItemDao()
        oItemView = ItemView()
        lista = oItemDao.carregarItensLoja()
        return oItemView.listarItens(lista)

    def cadastrarItem(self):
        oItemDao = ItemDao()
        oItemView = ItemView()
        idItem = oItemDao.maiorIdItem()
        from helpers import FormularioItem
        form = FormularioItem(idItem=idItem)
        return oItemView.cadastrarItem(form, aoEnviar='criarItem')

    def criarItem(self):
        from flask import request, redirect, flash, url_for
        from helpers import FormularioItem
        oItemDao = ItemDao()
        oItemView = ItemView()
        form = FormularioItem(request.form)
        if not form.validate_on_submit():
            flash('Erro ao criar item. Verifique os dados e tente novamente.','error')
            return redirect(oItemView.cadastrarItem(FormularioItem(idItem=oItemDao.maiorIdItem())))
        if oItemDao.itemExiste(form.nome.data):
            flash('Item já existe','error')
            return redirect(oItemView.cadastrarItem(FormularioItem(idItem=oItemDao.maiorIdItem())))
        oItemDao.criarNovoItem(form)
        flash('Item criado com sucesso!','success')
        return redirect(url_for('listarItens'))

    def deletarItem(self, idItem):
        oItemDao = ItemDao()
        oItemView = ItemView()
        oItemDao.deletarItem(idItem)
        flash('Item deletado com sucesso!', 'success')
        lista = oItemDao.carregarItensLoja()
        return oItemView.listarItens(lista)

    def editarItem(self, idItem):
        from helpers import FormularioItem
        oItemDao = ItemDao()
        oItemView = ItemView()
        item = oItemDao.carregarItemPorId(idItem)
        form = FormularioItem(obj=item)
        return oItemView.editarItem(form)

    def alterarItem(self):
        from flask import request, flash
        from helpers import FormularioItem
        oItemDao = ItemDao()
        oItemView = ItemView()
        form = FormularioItem(request.form)
        if not form.validate_on_submit():
            flash('Erro ao alterar item. Verifique os dados e tente novamente.','error')
            return oItemView.cadastrarItem(FormularioItem(idItem=oItemDao.maiorIdItem()))
        oItemDao.alterarItem(form)
        flash('Item alterado com sucesso!','success')
        lista = oItemDao.carregarItensLoja()
        return oItemView.listarItens(lista)