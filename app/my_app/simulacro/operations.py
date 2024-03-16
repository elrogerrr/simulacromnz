from sqlalchemy.orm import Session
from my_app.simulacro import models
from my_app import db

def getById(id:int):
    # user = db.session.query(models.User).filter(models.User.id==id).first()
    # user=models.User.query.get_or_404(id)
    user=db.session.query(models.Task).get(id)
    return user

def getAll():
    users=db.session.query(models.Task).all()
    return users

def create(name:str):
    userdb=models.Task(name=name)
    db.session.add(userdb)
    db.session.commit()
    db.session.refresh(userdb)
    return userdb

def update(id:int,name:str):
    userdb=getById(id=id)
    userdb.name=name
    db.session.add(userdb)
    db.session.commit()
    db.session.refresh(userdb)
    return userdb

def delete(id:int,show404=True):
    userdb=getById(id=id)
    db.session.delete(userdb)
    db.session.commit()
    
def pagination(page:int,size:int):
    models.Task.query.paginate(page,size)






