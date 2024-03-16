class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://elrogerrr:zapatanomurio666@localhost:3306/simulacromnz"
    SECRET_KEY='qwertyuioprogeliopoiuytrew'
    
