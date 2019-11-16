import pytest
from admin_userpermission_change import admin_userpermission_change
from auth_register import auth_register
from channels_create import channels_create
from data import *
import jwt


'''
Given a User by their user ID, set their permissions to new permissions described by permission_id

ValueError when:
    u_id does not refer to a valid user
    permission_id does not refer to a value permission

AccessError when:
    The authorised user is not an admin or owner

'''


def test_value_error_correct():
    owner = auth_register("hellothere@gmail.com", "SomePassword", "hello", "there")
    user = auth_register("z5160026@unsw.edu.au", "password", "whats", "up")

    admin_userpermission_change(owner['token'], user['u_id'], 1)

    i = False
    for j, items in data['users'].items():
        if items['u_id'] == user['u_id']:
            if items['permission'] == 1:
                i = True
    # at the end of this loop, the user being created has been promoted to owner
    assert i
      

def test_value_error_invalid_user():

    admin = auth_register("hello@gmail.com", "SomePassword", "hello", "there")
    user = auth_register("z5110036@unsw.edu.au", "password", "whats", "up")
    
    permission_id = 2

    #generate a fake token
    global SECRET
    SECRET = getSecret()
    token = jwt.encode({'u_id':500}, SECRET, algorithm='HS256').decode('utf-8')

    #change the permission of user who doesnt exist
    with pytest.raises(AccessError,match="Not a Valid Token"):
        admin_userpermission_change(token,user['u_id'], permission_id)

def test_value_error_invalid_permission():
    #setup
    admin = auth_register("helegfwelo@gmail.com", "SomePassword", "hello", "there")
    user = auth_register("z5110066@unsw.edu.au", "password", "whats", "up")


    #permission id is not valid (not 1, 2 or 3)
    with pytest.raises(ValueError,match="Invalid Permission"):
        admin_userpermission_change(admin['token'],user['u_id'], 5)

def test_access_error():
    #setup, admin
    test1 = auth_register("heergllo@gmail.com", "SomePassword", "hello", "there")
    test2 = auth_register("hellewfo@gmail.com", "SomePqgweassword", "hellwgeo", "theefqre")

    #test1 user is not an admin or owner
    with pytest.raises(AccessError,match="Not a admin"):
        admin_userpermission_change(test1['token'],test2['u_id'], 1)

def test_admin_demoted():
    
    #generate the token of the first owner
    global SECRET
    SECRET = getSecret()
    token = jwt.encode({'u_id':1}, SECRET, algorithm='HS256').decode('utf-8')

    user = auth_register("z5160926@unsw.edu.au", "password", "whats", "up")
    #make user a owner for a short time
    admin_userpermission_change(token, user['u_id'], 1)

    # owner changes user back to member
    admin_userpermission_change(token, user['u_id'], 3)
    i = False
    for j, items in data['users'].items():
        if items['u_id'] == user['u_id']:
            if items['permission'] == 3:
                i = True
    # at the end of this loop, the user being created has been promoted to owner
    assert i


