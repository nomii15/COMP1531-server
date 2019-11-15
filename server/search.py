#implementation of search function
from json import dumps
from flask import Flask,request, Blueprint
import jwt

from token_check import token_check
from token_to_uid import token_to_uid
from data import *

def Search_function(token, query_str):

    if token_check(token) == False:
        raise ValueError(description = "Invalid token")

    if len(query_str) > 1000:
        raise ValueError(description = "Message is greater than 1000 characters")    

    u_id = token_to_uid(token)

    global data
    data = getData()

    ret = {'messages': []}
    # for all channels, if the user is part of that channels
    # get the messages that 
    for i, items in data['channel_details'].items():
        for j in items['all_members']:
            #if they are apart of the channel, get messages
            if j['u_id'] == u_id:
                # the user is part of that channel
                # see if query exists
                for mess in data['channels'][ items['channel_id'] ]['messages']:
                    # see if the strings are in the messages
                    if query_str in mess['message']:
                        ret['messages'].append(mess)

    return ret 


Search_route = Blueprint('Search', __name__)
@Search_route.route('/search', methods=['GET'])
def Search_flask_route():
    token = request.args.get('token')
    query_str = str(request.args.get('query_str'))
    return dumps( Search_function(token, query_str) )

