'''
Given a User by their user ID, set their permissions to new permissions described by permission_id

ValueError when:
    u_id does not refer to a valid user
    permission_id does not refer to a value permission

AccessError when:
    The authorised user is not an admin or owner

'''

#definition admin_userpermission_change function
from flask import Flask, request, Blueprint
from json import dumps
from uid_check import uid_check
# importing the data file
from data import *
from token_check import token_check
from Error import *

adminChange = Blueprint('adminChange', __name__) 

@adminChange.route('admin/userpermission/change', methods=['POST'])
def admin_userpermission_change():
    
    token = request.form.get('token')
    u_id = request.form.get('u_id')
    permission_id = request.form.get('permission_id')

    if permission_id not in range(1,3):
        raise ValueError("not a valid permission")

    if token_check(token)==False:
        raise AccessError("Invalid Token")

    global SECRET
    SECRET = getSecret()
    Payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_idAdmin = Payload['u_id']

    if uid_check(u_id) == False:
        raise ValueError("Invalid u_id")

    global data
    data = getData()    

    if u_id not in data['channel_details']:
        raise AccessError("member not in channel")

    # get the channel associated with the token
    # need to check as only types of members are owners and others
    for i,items in data['channel_details'].items():
        if u_idAdmin == items['owner_members']:
            
            # modify the uid to change state of the user
            if permission_id == 1:
                # general member
                if u_id in items['owner_members']:
                    del(items['owner_member'])
            elif permission_id == 2:
                # owner
                items['owner_members'] = u_id


    raise AccessError("not a admin of the channel")            





    


