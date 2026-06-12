from flask import Flask
from flask_wtf.csrf import CSRFProtect
from database import bd  # 🌟 Importa o bd neutro do database.py
from sqlalchemy import event
from sqlalchemy.engine import Engine

app = Flask(__name__)

# 1. Carrega as configurações do config.py
app.config.from_pyfile('config.py')

# 2. Conecta o banco de dados ao aplicativo Flask (Resolve o AssertionError!)
bd.init_app(app)
csrf = CSRFProtect(app) 

# 3. Força o SQLite a aceitar Chaves Estrangeiras
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

# 4. Importa todos os Models para a memória
from models.UsuarioModel import UsuarioModel
from models.ItemModel import ItemModel
from models.EstoqueModel import EstoqueModel
from models.MundoModel import MundoModel
from models.ModuloModel import ModuloModel
from models.FaseModel import FaseModel
from models.ExercicioModel import ExercicioModel
from models.ProgressoModel import ProgressoModel



# 5. Agora sim, cria o banco e as tabelas com segurança
with app.app_context():
    bd.create_all()
    print("🚀 Banco SQLite 'pypo.db' e todas as tabelas foram gerados com sucesso!")

    # 🌟 IMPORTAÇÃO DOS MODELOS (Ajuste os nomes das classes/arquivos se necessário)
    from models.MundoModel import MundoModel
    from models.ModuloModel import ModuloModel
    from models.FaseModel import FaseModel

    # 🔍 CHECAGEM: Só alimenta se o banco realmente estiver zerado
    if not MundoModel.query.filter_by(idMundo=1).first():
        print("🌱 Banco vazio detectado! Inserindo dados iniciais obrigatórios...")
        
        try:
            # 1. Cria o Mundo
            novo_mundo = MundoModel(idMundo=1, linguagem="Mundo Inicial")
            bd.session.add(novo_mundo)
            
            # 2. Cria o Módulo
            novo_modulo = ModuloModel(idModulo=1, numero=1, nome="Introdução", idMundo=1)
            bd.session.add(novo_modulo)
            
            # 3. Cria a Fase 1
            nova_fase = FaseModel(idFase=1,materialApoio="", idModulo=1)
            bd.session.add(nova_fase)
            
            # Salva tudo no banco
            bd.session.commit()
            print("✨ Tabelas alimentadas com sucesso!")
            
        except Exception as e:
            bd.session.rollback()
            print(f"⚠️ Erro ao inserir dados iniciais: {e}")

# 6. Carrega as rotas por último
from views_user import *
from views_mundo import *
from views_funcionalidades import *

if __name__ == '__main__':
    app.run(debug=True)