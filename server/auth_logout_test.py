import pytest
from auth_logout import *


#dummy test cases for logout (since no return value) 


def test_auth_logout1():
    #create a test account
    register = auth_register("Someemial@hotmail.com.au", "Hello123", "First", "Last")
    
   #user is logged in, and logout is called
   
   auth_logout(register['token'])
   
   #this should successfully logout the user and deactivate the token
   
def test_auth_logout2():
       
   #create a test account
   register = auth_register("Someemial@hotmail.com.au", "Hello123", "First", "Last")
    
   #user is logged in, and logout is called
   #except in this test the token from register['token'] is not
   #the same as "#012" (a dummy token)
   
   auth_logout("#012")
   
   #this should not log the user out as the token passed in is not 
   #a valid token
   #
   #hence it should do anything
   
