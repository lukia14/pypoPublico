from database import bd

class MundoModel(bd.Model):
    __tablename__ = 'Mundo'
    idMundo = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    linguagem = bd.Column(bd.String(8), nullable=False, unique=True)
    modulo = bd.relationship('ModuloModel')
    def __repr__(self):
        return'<Mundo %r>' % self.linguagem
    
    def modeloMundo(self,form):
        linguagem = form.get('linguagem')
        novo_mundo = MundoModel(linguagem=linguagem)
        return novo_mundo
    
