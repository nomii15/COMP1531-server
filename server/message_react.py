'''
Given a users tokenID and a message Id and a react_id, react to a message

Value Errors-
    1. message_id not a valid message
    2. react_id is not valid
    2. message already is reacted to
'''

from flask import Flask, request, Blueprint
from json import dumps
from data import *
from Error import AccessError
from token_check import token_check
import jwt
from token_to_uid import token_to_uid


def message_react(token, message_id, react_id):
    
    if int(react_id) != 1:
        ret = {
            "code" : 400,
            "name": "ValueError",
            "message" : "Invalid react ID",
        }
        return dumps(ret)


    if token_check(token) == False:
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "Your idToken is invalid",
        }
        return dumps(ret)

    global data
    data = getData()

    u_id = token_to_uid(token)

    # get message
    for i,items in data['channels'].items():
        for item in items['messages']:
            if item['message_id']==int(message_id):
                for react in item['reacts']:
                    if react['react_id'] == int(react_id):
                        if u_id not in react['u_ids']:
                            react['u_ids'].append(u_id)
                        if u_id == item['u_id']:
                            react['is_this_user_reacted'] = True
                        else:
                            ret = {
                                "code" : 400,
                                "name": "ValueError",
                                "message" : "Message already reacted to",
                            }
                            return dumps(ret)
                        return dumps({}) 

    ret = {
        "code" : 400,
        "name": "AccessError",
        "message" : "Invalid Message ID",
        }
    return dumps(ret) 


react = Blueprint('react', __name__)
@react.route('/message/react', methods = ['POST'])
def route():
    message_id = request.form.get('message_id')
    token = request.form.get('token')
    react_id = request.form.get('react_id')

    return dumps(message_react(token, message_id, react_id))
