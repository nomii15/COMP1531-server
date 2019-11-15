'''
Given a users tokenID, send the message stored in the message parameter to the channel_id.

Value Errors-
    1. message being sent is greater than 1000 characters.
'''
from flask import Flask, request, Blueprint
from json import dumps
import jwt
from data import *
from datetime import datetime, timezone
from Error import AccessError
from token_check import token_check
from channel_check import id_check

#APP = Flask(__name__)
#send = Blueprint('send', __name__)
#@send.route('/message/send', methods = ['POST'])

def message_send(token, channel_id, message):

    #message = request.form.get('message')
    if (len(message) > 1000):
        ret = {
            "code" : 400,
            "name": "ValueError",
            "message" : "The message sent was too long",
        }
        return dumps(ret)
        #raise ValueError("Message too long")

    global data
    data = getData()

    #token = request.form.get('token')
    if token_check(token) == False:
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "Your idToken is invalid",
        }
        return dumps(ret)
        #raise AccessError('Invalid Token')
    
    
    #channel_id = request.form.get('channel_id')
    if id_check(int(channel_id)) == False:
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "You are trying to send a message to a channel you are not apart of",
        }
        return dumps(ret)


    global Message
    Message = getMessage()
    print('just ran getmessage. messageID = ')
    print(Message)
    now = datetime.now()
    timestamp = now.replace(tzinfo=timezone.utc).timestamp()
    currentTime = timestamp
    #currentTime = now.strftime("%H:%M:%S")
    reacts = [{
        'react_id': Message,
        'u_ids': [],
        'is_this_user_reacted': False
    }]
    is_pinned = False
    #message_id = Message

    global SECRET
    SECRET = getSecret()
    
    #extract u_id from token
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = int(token_payload['u_id'])
    #print(u_id)
    
    new_message = {
        'message_id': Message,
        'u_id': u_id,
        'message': message,
        'time_created': currentTime,
        'reacts': reacts,
        'is_pinned': is_pinned
    }
    
    for d,j in data['channels'].items():
        if j['channel_id'] == int(channel_id):
            data['channels'][d]['messages'].append(new_message)
            ret = {'message_id': Message}
            incMessage()
            print('just ran incMessage. messageID = ')
            return dumps({'message_id': Message})
            

    


send = Blueprint('send', __name__)
@send.route('/message/send', methods = ['POST'])
def route():
    message = request.form.get('message')
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')

    return dumps(message_send(token, channel_id, message))
#if __name__ == '__main__':
#    APP.run(debug=True)

