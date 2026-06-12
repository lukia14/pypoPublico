from flask import render_template

class ItemView:
    def __init__(self):
        pass

    def loja(self,listaItens,listaEstoque,pontuacao):
        return render_template('loja.html', listaItens=listaItens, listaEstoque=listaEstoque,pontuacao=pontuacao)
    
    def listarItens(self, listaItens):
        return render_template('listarItens.html', listaItens=listaItens)

    def cadastrarItem(self, form, aoEnviar='criarItem'):
        return render_template('cadastroItem.html', form=form, titulo='Criar Item', aoEnviar=aoEnviar)

    def editarItem(self, form):
        return render_template('cadastroItem.html', form=form, titulo='Editar Item', aoEnviar='alterarItem')
    