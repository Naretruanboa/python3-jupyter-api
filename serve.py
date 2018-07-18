# install Flask framework using pip3 install flask
from flask import Flask, request
import json

app = Flask('simple_api')
UserJson = [
    {
        'name'  : 'naret',
        'last'  : 'ruanboa',
        'email' : 'naret_ruanboa@hotmail.com',
        'No.'   : '1234567890XX'
    } , {
        'name'  : 'test',
        'last'  : 'xxxx',
        'email' : 'test@hotmail.com',
        'No.'   : '135453423312'
    }
]

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return json.dumps(UserJson)
    else:
        return json.dumps({'response':'Hello in POST method'})

@app.route('/login/<username>', methods=['GET'])
def login(username):
    if request.method == 'GET':
        return json.dumps({'response':'Hi %s' % username})
    
# $ env FLASK_APP=serve.py flask run




