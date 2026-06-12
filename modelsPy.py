from app import bd
class Mundo(bd.Model):
    idMundo = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    linguagem = bd.Column(bd.String(8), nullable=False, unique=True)
    modulo = bd.relationship('Modulo')
    def __repr__(self):
        return'<Mundo %r>' % self.linguagem
    


    

    