from flask import g,Blueprint, flash, redirect, url_for, render_template
from flask_login import current_user, login_user, logout_user, login_required
from my_app import login_manager,db
from my_app.auth.models import User
from my_app.auth.forms import RegistrationForm,LoginForm

authRoute=Blueprint('auth',__name__)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@authRoute.before_request
def get_current_user():
    g.user=current_user
    
@authRoute.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        flash('tu estas logieado en')
        return redirect(url_for('simulacro.index'))
    form=RegistrationForm()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        existing_username=User.query.filter_by(username=username).first()
        if existing_username:
            flash('Este nombre ya esta usado. try ahother one','warning')
            return render_template('dashboard/user/register.html',form=form)
        user=User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        flash('ya stas, porfagor logeate','sussess')  
        if form.errors:
            flash(form.errors,'danger')
        else:
            return redirect(url_for('auth.login'))
    return render_template('dashboard/user/register.html',form=form)

@authRoute.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        flash('tu estas logieado en')
        return redirect(url_for('simulacro.index'))
    
    form=LoginForm()
    
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        existing_user=User.query.filter_by(username=username).first()
        if not(existing_user and existing_user.check_password(password)):
            flash('usuario o password incorrecto','warning')
            return render_template('dashboard/user/login.html',form=form)
            
        login_user(existing_user) 
        flash('ya stas peinado pa tras','success')   
        return redirect(url_for('simulacro.index'))

    if form.errors:
        flash(form.errors,'danger')
    return render_template('dashboard/user/login.html',form=form)

@authRoute.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    