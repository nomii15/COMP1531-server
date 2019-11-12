from flask import Flask, request, Blueprint
from data import *
from token_check import token_check
from json import dumps

def users_all(token):
    
    global data
    data = getData()

    #return dictionary
    ret = {
        'users': []
    }
    temp = {}

    for i, items in data['users'].items():
        #print(items)
        temp = {
            'u_id': items['u_id'],
            'email': items['email'],
            'name_first': items['name_first'],
            'name_last': items['name_last'],
            'handle_str': items['handle'],
            'profile_img_url': items['profile_img_url']
        }
        ret['users'].append(temp)
    return ret    
        


# get all users and return 
Uall = Blueprint('Uall',__name__)
@Uall.route('/users/all', methods=['GET'])
def users_all_route():
    token = str(request.args.get('token'))
    return dumps(users_all(token))



