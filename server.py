"""Flask server"""
import sys
from flask_cors import CORS
from flask import Flask, request, jsonify, send_from_directory
from json import dumps
from werkzeug.exceptions import HTTPException
from flask_mail import Mail, Message


# if running on your computer, change path
sys.path.insert(1,'/tmp_amd/cage/export/cage/3/z5110036/comp1531/project/W15A-DJMN/server/')
from auth_login import login
from auth_logout import logout
from auth_register import register
from auth_passwordreset_request import requestR
from auth_passwordreset_reset import reset
from channel_messages import channel_message
from search import Search
from channels_create import Channels_create
from channels_list import Channels_list
from channels_listall import Channels_listall
from channel_details import DETAILS
from channel_invite import INVITE
from channel_join import join
from channel_leave import leave
from message_send import send
from user_profile import PROFILE
from user_profile_sethandle import SETHANDLE
from user_profile_setmail import SETMAIL
from user_profile_setname import SETNAME
from message_edit import edit
from message_remove import remove
from message_react import react
from message_unreact import unreact
from message_pin import pin
from message_unpin import unpin
from users_all import Uall
from user_profiles_uploadphoto import uploadphoto
from standup_active import active
from standup_start import start
from standup_send import standsend
'''
def defaultHandler(err):
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.description,
    })
    response.content_type = 'application/json'
    return response
'''

def defaultHandler(err):
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.description,
    })
    response.content_type = 'application/json'
    return response


APP = Flask(__name__, static_url_path='/static/')
APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)
CORS(APP)



APP.register_blueprint(register)
APP.register_blueprint(login)
APP.register_blueprint(logout)
APP.register_blueprint(requestR)
APP.register_blueprint(reset)
APP.register_blueprint(channel_message)
APP.register_blueprint(Search)
APP.register_blueprint(Channels_create)
APP.register_blueprint(Channels_list)
APP.register_blueprint(Channels_listall)
APP.register_blueprint(DETAILS)
APP.register_blueprint(INVITE)
APP.register_blueprint(join)
APP.register_blueprint(leave)
APP.register_blueprint(send)
APP.register_blueprint(PROFILE)
APP.register_blueprint(SETHANDLE)
APP.register_blueprint(SETMAIL)
APP.register_blueprint(SETNAME)
APP.register_blueprint(edit)
APP.register_blueprint(remove)
APP.register_blueprint(react)
APP.register_blueprint(unreact)
APP.register_blueprint(pin)
APP.register_blueprint(unpin)
APP.register_blueprint(Uall)
APP.register_blueprint(uploadphoto)
APP.register_blueprint(active)
APP.register_blueprint(standsend)
APP.register_blueprint(start)
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

@APP.route('/static/<path:path>')
def send_js(path):
    return send_from_directory(APP.static_url_path , path)
    

if __name__ == '__main__':
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000))


