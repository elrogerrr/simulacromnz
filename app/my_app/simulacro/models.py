from sqlalchemy.orm import relationship
from sqlalchemy import Column,String,Integer,DateTime
from my_app import db
from datetime import datetime
    
class Area(db.Model):
    __tablename__='areas'
    id=db.Column(db.Integer, primary_key=True)
    area=db.Column(db.String(255))
    p_total=db.Column(db.Integer,nullable=False)
    p_actual=db.Column(db.Integer,nullable=False)
    p_rezago=db.Column(db.Integer,nullable=True)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
    
class Historial(db.Model):
    __tablename__='historial'
    id=db.Column(db.Integer, primary_key=True)
    h_brigadista_id=db.Column(db.Integer, nullable=False)
    h_brigadista_name=db.Column(db.String(255), nullable=False)
    h_area_created_at=db.Column(db.DateTime,default=datetime.utcnow)
    h_area_id=db.Column(db.Integer, nullable=False)
    h_area_p_total=db.Column(db.Integer,nullable=False)
    h_area_p_actual=db.Column(db.Integer,nullable=False)
    h_area_p_rezago=db.Column(db.Integer,nullable=False)
    