#definition channels_listall function
from flask import Flask, request, Blueprint
from json import dumps
from Error import AccessError

# importing the data file
from data import *
from token_check import *

'''
Provide a list of all channels (and their associated details)

'''

channels_listall = Blueprint('APP_listall', __name__)
@channels_listall.route('channels/listall', methods['GET'])
def channels_listall():
    token = request.args.get('token')
    if token_check(token) == False:
        raise AccessError('Invalid Token')
    #add channel dictionary to add to global dictionary
    global data
    data = getData()

    ret = dict()

    for channel in data['channel'].items():
        del data['channel'][channel]['messages']
        del data['channel'][channel]['is_public']
        ret[channel] = data['channel'][channel]#[['name']['channel_id']] <= check how to only return these two fields 

    return dumps(ret)