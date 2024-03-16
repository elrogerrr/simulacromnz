from flask import Blueprint, redirect, url_for, render_template, request,g,session
from my_app.simulacro.models import Task
from my_app.auth import models
from my_app.simulacro import forms
from my_app.auth import controllers
from my_app.simulacro import operations
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
    username=controllers.current_user.username
    return render_template('dashboard/index.html',username=username,user=operations.getAll())

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
    return render_template('dashboard/evento/update.html')



