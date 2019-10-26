from flask import Flask, request, Blueprint
from json import dumps
from data import *
from uid_check import *
from channel_check import *

invite = Blueprint('invite', __name__)

@invite.route('/channel/invite', methods=['POST'])
def channel_invite():
    data = getData()
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))
    invitee = request.form.get('u_id')
    
    
    
    if member_check(token, channel_id) == False:
        raise AccessError("inviter is not a member of the given channel.")
        
    if ...:
        raise ValueError("channel_id does not refer to a valid channel that the authorised user is part of.")
        
    if uid_check(invitee) == False:
        raise ValueError("invalid u_id.")
        
    data['channel_details']['channel_id']['all_members'].append(invitee)
