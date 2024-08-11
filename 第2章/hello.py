#$pip install flask

from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

'''
$set flask_app=hello.py
$set flask_debug=1
$flask run
'''
@app.route('/user')
def user(name):
    return '<h1>Hello,{}</h1>'.format(name)

'''
$python
>>>from hello import app
>>>from flask import current_app
>>>app_ctx=app.app_context()
>>>app_ctx.push
>>>current_app.name
'hello'
>>>app_ctx.pop()
'''

'''
$python
>>>from hello import app
>>>app.url_map
'''