"""Flask server"""
import sys
from flask_cors import CORS
from json import dumps
from flask import Flask, request
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

APP = Flask(__name__)
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


