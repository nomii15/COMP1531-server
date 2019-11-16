'''
Given a users tokenID and a message Id and a react_id, unreact to a message

Value Errors-
    1. message_id not a valid message
    2. react_id is not valid
    2. message not reacted to
'''


from flask import Flask, request, Blueprint
from json import dumps
from data import *
import jwt
from Error import AccessError
from token_check import token_check


def message_unreact(token, message_id, react_id):
    
    if int(react_id) != 1:
        print('invalid react id')
        ret = {
            "code" : 400,
            "name": "ValueError",
            "message" : "Invalid react ID",
        }
        return dumps(ret)

    if token_check(token) == False:
        print('invalid token id')
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "Your idToken is invalid",
        }
        return dumps(ret)

    global data
    data = getData()

    global SECRET 
    SECRET = getSecret()
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = token_payload['u_id']

    for i, items in data['channels'].items():
        for item in items['messages']:
            if item['message_id']==int(message_id):
                for react in item['reacts']:
                    if react['react_id'] == int(react_id): 
                        if u_id in react['u_ids']:
                            react['u_ids'].remove(u_id)
                        if u_id == item['u_id']:
                            react['is_this_user_reacted'] = False
                        else:
                            ret = {
                                "code" : 400,
                                "name": "ValueError",
                                "message" : "Message already unreacted",
                            }
                            return dumps(ret)
                        return dumps({}) 

    ret = {
        "code" : 400,
        "name": "AccessError",
        "message" : "Invalid Message ID",
        }
    return dumps(ret) 

                        
unreact = Blueprint('unreact', __name__)
@unreact.route('/message/unreact', methods = ['POST'])
def route():
    message_id = request.form.get('message_id')
    token = request.form.get('token')
    react_id = request.form.get('react_id')

    return dumps(message_unreact(token, message_id, react_id))