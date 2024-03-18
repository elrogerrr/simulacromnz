from sqlalchemy.orm import session
from my_app.auth import models
from my_app import db

def getById(id:int):
    # user = db.session.query(models.User).filter(models.User.id==id).first()
    # user=models.User.query.get_or_404(id)
    user=db.session.query(models.User).get(id)
    return user

def getAll():
    users=db.session.query(models.User).all()
    return users