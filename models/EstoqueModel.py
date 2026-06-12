from database import bd
class EstoqueModel(bd.Model):
    __tablename__ = 'Estoque'
    qtd = bd.Column(bd.Integer, nullable=False)
    idUsuario = bd.Column(bd.Integer, bd.ForeignKey('Usuario.idUsuario'), primary_key=True)
    idItem = bd.Column(bd.Integer, bd.ForeignKey('Item.idItem'), primary_key=True)
    
    def __repr__(self):
        return'<Estoque %r>' % self.qtd