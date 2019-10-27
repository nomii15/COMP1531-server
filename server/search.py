#implementation of search function
from json import dumps
from flask import Flask,request, Blueprint
import jwt

from token_check import token_check
from data import *

search = Blueprint('search', __name__)


@search.route('/search', methods=['GET'])
def search():
    ret = {'messages': []}

    token = request.args.get('token')
    query_str = request.args.get('query_str')

    if token_check(token) == False:
        raise ValueError("Invalid token")

    global SECRET
    SECRET = getSecret()
    Payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = Payload['u_id'] 

    global data
    data = getData()

    # for all channels, if the user is part of that channels
    # get the messages that 
    for i, items in data['channel_details'].items():
        for j in items['all_members']:
            if j == u_id:
                # the user is part of that channel
                # see if query exists
                if query_str in items['messages']:
                    ret['messages'].append(items['messages'])

    return dumps(ret)            

