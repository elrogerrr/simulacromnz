from sqlalchemy.orm import relationship
from my_app import db

class Task(db.Model):
    __tablename__='task'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255))
    
# class Area(db.Model):
#     __tablename__='area'
#     id=db.Column(db.Integer, primary_key=True)
#     area=db.Column(db.String(255))
#     p_total=db.Column(db.Integer,nullable=False)
#     p_actual=db.Column(db.Integer,nullable=False)
#     p_rezago=db.Column(db.Integer,nullable=False)
