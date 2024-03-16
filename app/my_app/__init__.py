from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from my_app.config import DevConfig, ProdConfig
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_login import LoginManager


app=Flask(__name__)
app.config.from_object(DevConfig)
bootstrap = Bootstrap5(app)

db=SQLAlchemy(app)
migrate=Migrate(app,db)

login_manager=LoginManager()
login_manager.init_app(app)

from my_app.simulacro.controllers import simulacroRoute
app.register_blueprint(simulacroRoute)
from my_app.auth.controllers import authRoute
app.register_blueprint(authRoute)

