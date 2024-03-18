from flask import Blueprint, redirect, url_for, render_template, request,g,session
from my_app.simulacro.models import Area,Historial
from my_app.auth import models
from my_app.simulacro import forms 
from my_app.auth import controllers
from my_app.simulacro import operations
from my_app.auth import operations as operationsdb
from flask_login import login_required, current_user

simulacroRoute=Blueprint('simulacro',__name__,url_prefix='/simulacro')

task_list=[1,2,3,4,5,6]

@simulacroRoute.before_request
@login_required
def before():
    pass

@simulacroRoute.route('/')
# @login_required
def index():
    area=operations.getAll()
    username=controllers.current_user.username
    user_id=controllers.current_user.id
    b_id=Area.query.filter(Area.id.like(user_id)).all()
    return render_template('dashboard/index.html',user_id=user_id,
                                                b_id=b_id,
                                                username=username,
                                                area=area)

@simulacroRoute.route('/<int:id>')
def show(id:int):
    return 'la de show... ' + str(id)

@simulacroRoute.route('/delete/<int:id>')
def delete(id:int):
    operations.delete(id)
    return redirect(url_for('simulacro.index'))

@simulacroRoute.route('/create', methods=('GET','POST') )
def create():
    form=forms.Usuario()
    if form.validate_on_submit():
        print(form.name.data)
        operations.create(form.name.data)
    return render_template('dashboard/evento/create_user.html',form=form)

@simulacroRoute.route('/update/<int:id>', methods=('GET','POST') )
def update(id:int):
    
    evento=operations.getById(id)
    form=forms.Evento()
    
    if request.method=='GET':
        form.p_actual.data=evento.p_actual
        form.p_rezago.data=evento.p_rezago
    if form.validate_on_submit():
        operations.update(id,form.p_actual.data,form.p_rezago.data)
    
    return render_template('dashboard/evento/update.html',form=form)

@simulacroRoute.route('/monitor')
def monitor():
    username=controllers.current_user.username
    user=operationsdb.getAll()
    print(user)
    print(username)
    return render_template('dashboard/monitor.html',username=username,user=user)



