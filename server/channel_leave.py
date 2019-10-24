#definition channel_leave function
from flask import Flask, request, Blueprint

# importing the data file
from data import *
from token_check import *

'''
Given a channel ID, the user removed as a member of this channel.

ValueError when:
        Channel (based on ID) does not exist.

'''

channel_leave = Blueprint('APP_leave', __name__)
@channel_leave.route('channels/leave', methods['POST'])
def channel_leave(token, channel_id):
    pass
