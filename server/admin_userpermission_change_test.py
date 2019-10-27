import pytest
from admin_userpermission_change import admin_userpermission_change
from auth_register_test import testRegister

'''
Given a User by their user ID, set their permissions to new permissions described by permission_id

ValueError when:
    u_id does not refer to a valid user
    permission_id does not refer to a value permission

AccessError when:
    The authorised user is not an admin or owner

'''

class admin():
    def __init__(self, perm):
        self.permission = perm
    def per(self):
        if self.permission>3 or self.permission<1:
            raise ValueError("Invalid Permission")
    def setadmin(self, a):
        self.admin = a
    def isAdmin(self):
        if self.admin!=1:
            raise ValueError("Not a admin")         

def test_value_error_invalid_user():

    test = testRegister("hello@gmail.com", "SomePassword", "hello", "there")

    permission_id = 2

    #change the permission of user who doesnt exist
    with pytest.raises(ValueError,match="Not a Valid Token"):
        test.uid(1)

def test_value_error_invalid_permission():
    #setup
    test = testRegister("hello@gmail.com", "SomePassword", "hello", "there")
    permission_id = 5
    t = admin(permission_id)


    #permission id is not valid (not 1, 2 or 3)
    with pytest.raises(ValueError,match="Invalid Permission"):
        t.per()

def test_access_error():
    #setup, admin
    test1 = testRegister("hello@gmail.com", "SomePassword", "hello", "there")
    admin1 = admin(2)
    #not an admin, trying to add test2 to a group
    admin1.setadmin(0)
    #user
    test2 = testRegister("hellewfo@gmail.com", "SomePqgweassword", "hellwgeo", "theefqre")


    #authorised user is not an admin or owner
    with pytest.raises(ValueError,match="Not a admin"):
        admin1.isAdmin()
