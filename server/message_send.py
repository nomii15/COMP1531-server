'''
Given a users tokenID, send the message stored in the message parameter to the channel_id.

Value Errors-
    1. message being sent is greater than 1000 characters.
'''
from flask import Flask, request, Blueprint
from json import dumps
#from channels_list import channels_list
import jwt
from data import *
from datetime import datetime, timezone
from Error import AccessError
from token_check import token_check
from channel_check import id_check

#APP = Flask(__name__)
send = Blueprint('send', __name__)
@send.route('/message/send', methods = ['POST'])
def message_send():

    message = request.form.get('message')
    if (len(message) > 1000):
        raise ValueError("Message too long")

    global data
    data = getData()

    #the access errors not working at the moment with postman. commented out for the moment

    token = request.form.get('token')
    if token_check(token) == False:
        raise AccessError('Invalid Token')
    
    
    channel_id = request.form.get('channel_id')
    if id_check(int(channel_id)) == False:
        print("error")
        return
    #list_of_channels =  channels_list(token)
    #if not any(d['channel_id'] == channel_id for d in list_of_channels):
    #    print('Access error')
    #    return
    
    length = 0
    for d,j in data['channels'].items(): 
        #print(j)
        if j['channel_id'] == channel_id:
            length = len(d['messages']) + 1
            break
    
    now = datetime.now()
    timestamp = now.replace(tzinfo=timezone.utc).timestamp()
    currentTime = timestamp
    #currentTime = now.strftime("%H:%M:%S")
    reacts = [{
        'react_id': length,
        'u_ids': [],
        'is_this_user_reacted': False
    }]
    is_pinned = False
    message_id = length

    global SECRET
    SECRET = getSecret()
    
    #extract u_id from token
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = int(token_payload['u_id'])
    #print(u_id)
    
    new_message = {
        'message_id': message_id,
        'u_id': u_id,
        'message': message,
        'time_created': currentTime,
        'reacts': reacts,
        'is_pinned': is_pinned
    }
    for d,j in data['channels'].items():
        #print(j)
        #print(channel_id)
        if j['channel_id'] == int(channel_id):
            #print("somethings")
            data['channels'][d]['messages'].append(new_message)
            ret = {'message_id': message_id}
            #print(new_message)
            return dumps({'message_id': message_id})
            

        
        
    ret = {'message_id': message_id}
    return dumps(ret)

#if __name__ == '__main__':
#    APP.run(debug=True)

