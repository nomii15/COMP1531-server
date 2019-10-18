"""Flask server"""
import sys
from flask_cors import CORS
from json import dumps
from flask import Flask, request



APP = Flask(__name__)
CORS(APP)

@APP.route('/echo/get', methods=['GET'])
def echo1():
    """ Description of function """
    return dumps({
        'echo' : request.args.get('echo'),
    })

@APP.route('/echo/post', methods=['POST'])
def echo2():
    """ Description of function """
    return dumps({
        'echo' : request.form.get('echo'),
    })

@APP.route('/auth/register', methods=['POST'])
def register():
    return server.auth_register()

@APP.route('/auth/login', methods=['POST'])
def login():
    return server.auth_login()

@APP.route('/auth/logout', methods=['POST'])
def logout():
    return server.auth_logout()        


if __name__ == '__main__':
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000))
