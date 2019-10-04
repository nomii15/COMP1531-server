import pytest
from auth_passwordreset_request import *


#invalid email
def test_auth_passwordreset_request1():

    #create a test account
    register = auth_register("Someemial@hotmail.com.au", "Hello123", "First", "Last")
    
    #this will throw an exception as the email entered isnt a valid email
    with pytest.raises(ValueError, match = '*Invalid Email Address*'):
        auth_passwordreset_request("someemail.com")
        
#email not registered
def test_auth_passwordreset_request2():

    #assumes an account for the email address doesnt exist
    
    #this throws an error as the email is not belonging to a register user
    with pytest.raises(ValueError, match = '*Not a Registed Email Address*'):
        auth_passwordreset_request("z5260026@unsw.edu.au")
        
#valid
def test_auth_passwordreset_request3():

    #create a test account
    register = auth_register("Someemial@hotmail.com.au", "Hello123", "First", "Last")
    
    #ask for a password reset
    auth_passwordreset_request("Someemail@hotmail.com.au")
    
    #this test should work and send a code to the users email address
    
         
