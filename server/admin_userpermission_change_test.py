import pytest
import admin_userpermission_change from admin_userpermission_change
import auth_register from auth_register

'''
Given a User by their user ID, set their permissions to new permissions described by permission_id

ValueError when:
    u_id does not refer to a valid user
    permission_id does not refer to a value permission

AccessError when:
    The authorised user is not an admin or owner

'''

def test_value_error_invalid_user():
    #setup
    register1 = auth_register("hello@gmail.com","abc","hi","hello")
    token1 = register1['token']
    u_id1 = register1['u_id']

    permission_id = 2

    #user id does not exist
    with pytest.raises(ValueError,match=r"*"):
        admin_userpermission_change(token1,u_id2, permission_id)

def test_value_error_invalid_permission():
    #setup
    register1 = auth_register("hello@gmail.com","abc","hi","hello")
    token1 = register1['token']
    u_id1 = register1['u_id']

    register2 = auth_register("helloo@gmail.com","abcd","hihi","helloo")
    token2 = register2['token']
    u_id2 = register2['u_id']

    permission_id = 5

    #permission id is not valid (not 1, 2 or 3)
    with pytest.raises(ValueError,match=r"*"):
        admin_userpermission_change(token1, u_id2, permission_id)

def test_access_error():
    #setup
    register1 = auth_register("hello@gmail.com","abc","hi","hello")
    token1 = register1['token']
    u_id1 = register1['u_id']

    register2 = auth_register("helloo@gmail.com","abcd","hihi","helloo")
    token2 = register2['token']
    u_id2 = register2['u_id']

    permission_id = 2

    #authorised user is not an admin or owner
    with pytest.raises(ValueError,match=r"*"):
        admin_userpermission_change(token2, u_id1, permission_id)
