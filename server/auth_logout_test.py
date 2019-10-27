import pytest
from auth_logout import auth_logout
from auth_register_test import testRegister


#dummy test cases for logout (since no return value)
class testLogout():
    def __init__(self):
        self.id = 0
        self.token = 0
    def logout(self,u_id, token):
        if u_id == 0:
            self.token=None
        else:
            raise ValueError("Invalid Token")    



        



def test_auth_logout1():
    #create a test account
    register = testRegister("Someemial@hotmail.com.au", "Hello123", "First", "Last")
    test = register.valid()
    #user is logged in, and logout is called
    log = testLogout()
    log.logout(test['u_id'], test['token'])
    assert log.token == None
   
    #this should successfully logout the user and deactivate the token
   
def test_auth_logout2():
       
    register = testRegister("Someemial@hotmail.com.au", "Hello123", "First", "Last")
    test = register.valid()
    #user is logged in, and logout is called
    log = testLogout()
    log.logout(test['u_id'], "notacorrecttoken")
   
    with pytest.raises(ValueError, match='*Invalid Token*'):
        log.logout("1", "notacorrecttoken")
    
    #this should not log the user out as the token passed in is not 
    #a valid token
   
