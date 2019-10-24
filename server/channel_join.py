#definition channels_listall function
from flask import Flask, request, Blueprint

# importing the data file
from data import *
from token_check import *

'''
Given a channel_id of a channel that the authorised user can join, adds them to that channel

ValueError when:
    Channel (based on ID) does not exist
AccessError when:
    channel_id refers to a channel that is private (when the authorised user is not an admin)
'''

channel_join = Blueprint('APP_listall', __name__)
@channel_join.route('channels/listall', methods['POST'])
def channel_join(token, channel_id):
    pass