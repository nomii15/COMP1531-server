"""Flask server"""
import sys
from flask_cors import CORS
from json import dumps
from flask import Flask, request
from flask_mail import Mail, Message


sys.path.insert(0,'/tmp_amd/cage/export/cage/3/z5110036/comp1531/project/W15A-DJMN/server/')
from auth_login import login
from auth_logout import logout
from auth_register import register
from auth_passwordreset_request import requestR
from auth_passwordreset_reset import reset


APP = Flask(__name__)
CORS(APP)


APP.register_blueprint(register)
APP.register_blueprint(login)
APP.register_blueprint(logout)
APP.register_blueprint(requestR)
APP.register_blueprint(reset)
'''
mail = Mail(APP) 
APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'DJMN1531@gmail.com',
    MAIL_PASSWORD = "password1531"  
                )
'''




'''
@APP.route('/auth/register', methods=['POST'])
def echo4():
    pass
'''    

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

if __name__ == '__main__':
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000))


