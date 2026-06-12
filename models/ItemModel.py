from database import bd

class ItemModel(bd.Model):
   __tablename__ = 'Item'
   idItem = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
   nome = bd.Column(bd.String(25), nullable=False)
   descricao = bd.Column(bd.String(99), nullable=False)
   valor = bd.Column(bd.Integer, nullable=False)

   def __repr__(self):
        return'<Item %r>' % self.nome