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
from token_to_uid import token_to_uid
from Error import AccessError


def admin_userpermission_change(token, u_id, permission_id):

    if permission_id > 3 or permission_id < 1:
        raise ValueError(description = "not a valid permission")

    if token_check(token)==False:
        raise AccessError("Invalid Token")

    u_idAdmin = token_to_uid(token)

    if uid_check(u_idAdmin) == False:
        raise ValueError(description = "Invalid u_id")

    global data
    data = getData()    

    # check if the admin is actually a admin or owner
    for j, item in data['users'].items():
        if u_idAdmin == item['u_id']:
            #if there permission is 3, they dont have the ability to promote a user
            if item['permission'] == 3:
                raise AccessError("User trying to change permission is not a admin or owner or slackr")
            else:
                # permision is one or two, meaning they are either a admin or a owner of slackr
                break    

    # get the channel associated with the token
    # need to check as only types of members are owners and others
    for i,items in data['users'].items():
        if u_id == items['u_id']:
            
            #check to see which type the user is, if its the same, dont do anything
            if permission_id == items['permission']:
                return {}
                
            if permission_id < items['permission']:
                # meaning the permission of the user is increasing (admin to owner or general to admin)
                if permission_id == 2:
                    items['permission'] = 2
                if permission_id == 1:
                    items['permission'] = 1
                
                user = {'u_id': items['u_id'], 'name_first': items['name_first'], 'name_last': items['name_last']}
                #need to go through each channel and add admin and owner users as owners of every channel
                for k, chan in data['channel_details'].items():
                    if items['u_id'] in chan['all_members']:
                        chan['owner_members'].append(user)    
            else:
                #downgrade from one level to another
                #only need to remove owner from channel if they are going from admin on general member
                #also need to check if they user created the channel
                user = {'u_id': items['u_id'], 'name_first': items['name_first'], 'name_last': items['name_last']}
                if permission_id == 3:
                    for l, check in data['channel_details'].items():
                        if check['creator'] == u_id:
                            #if they created the channel, dont remove there status as owner of that channel
                            continue
                        if u_id in check['owner_member']:
                            check['owner_member'].remove(user)
                items['permission'] = permission_id

    return {}           





adminChange = Blueprint('adminChange', __name__) 

@adminChange.route('/admin/userpermission/change', methods=['POST'])
def admin_route():
    token = request.form.get('token')
    u_id = int(request.form.get('u_id'))
    permission_id = int(request.form.get('permission_id'))
    #print(permission_id)
    return dumps( admin_userpermission_change(token, u_id, permission_id) )




    


