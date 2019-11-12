import pytest
from auth_logout import auth_logout
from auth_register import auth_register
from data import *


#dummy test cases for logout (since no return value) 


def test_auth_logout1():
    #create a test account
    register = auth_register("Someemial@hotmail.com.au", "Hello123", "First", "Last")
    
    #user is logged in, and logout is called
   
    assert auth_logout(register['token'])
   
    #this should successfully logout the user and deactivate the token
   
def test_auth_logout2():
       
    #create a test account
    register = auth_register("email@hotmail.com.au", "Hello123", "First", "Last")
    
    # log out the user
    auth_logout(register['token'])
   
   #attempt to logout the user who isnt logged in
    assert auth_logout(register['token']) == False
    
    #this should not log the user out as the token passed in is not 
    #a valid token
   
