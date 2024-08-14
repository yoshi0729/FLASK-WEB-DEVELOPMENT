from flask import Flask,abort,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app=Flask(__name__)
bootstrap=Bootstrap(app)
moment=Moment(app)

app.config['SECRET_KEY']='hard to guess string'

class NameForm(FlaskForm):
    name=StringField('What is your name?',validators=[DataRequired()])
    submit=SubmitField('submit')

@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name=session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('名前が変更されたようです')
        session['name']=form.name.data
        form.name.data=''
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'),current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

@app.route('/error')
def trigger_error():
    abort(500)

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

#-------ターミナル-------
#pip install flask-wtf