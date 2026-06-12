import os
caminho_projeto = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(caminho_projeto, 'pypo.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'pudim'