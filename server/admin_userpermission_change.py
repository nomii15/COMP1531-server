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

adminChange = Blueprint('adminChange', __name__) 

@adminChange.route('admin/userpermission/change', methods=['POST'])
def admin_userpermission_change():
    
    token = request.form.get('token')
    u_id = request.form.get('u_id')
    permission_id = request.form.get('permission_id')

    if not uid_check(u_id):
        raise ValueError("Invalid u_id")

     # check valid permission

     # check authorised user

     # data structure needed for owners and admins   

    global data
    data = getData()



