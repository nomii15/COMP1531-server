'''
Given a users tokenID and a message Id, unpin the message

Value Errors-
    1. message_id not a valid message
    2. authorised user is not an admin
    3. message not pinned
AccessError-
    1. Authorised user is not a memeber of channel
'''
from flask import Flask, request, Blueprint
from json import dumps
from data import *
from Error import AccessError
from token_check import token_check
from check_channel_owner import channel_owner
import jwt
from token_to_uid import token_to_uid

def message_unpin(token, message_id):
    if token_check(token) == False:
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "Your idToken is invalid",
        }
        return dumps(ret)
    
    global data
    data = getData()

    # retrieve u_id from token
    #global SECRET 
    #SECRET = getSecret()
    #token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    #uid = token_payload['u_id']
    u_id = token_to_uid(token)
    # find the message and modify the pin operation
    for i, items in data['channels'].items():
        print(i)
        for item in items['messages']:
            if item['message_id']==int(message_id):
                print("got message id")
                if channel_owner(items['name'], u_id) == True:
                    if item['is_pinned']==True:
                        item['is_pinned']=False
                        print(item)
                        return dumps({})
                    else:
                        ret = {
                            "code" : 400,
                            "name": "ValueError",
                            "message" : "Message is already already unpinned",
                        }
                        return dumps(ret)  
                else :
                    ret = {
                        "code" : 400,
                        "name": "ValueError",
                        "message" : "The authorised user is not an admin",
                    }
                    return dumps(ret) 


unpin = Blueprint('unpin', __name__)
@unpin.route('/message/unpin', methods = ['POST'])
def route():
    message_id = request.form.get('message_id')
    token = request.form.get('token')
    
    return dumps(message_unpin(token, message_id))

