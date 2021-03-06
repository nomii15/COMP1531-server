import pytest
from auth_passwordreset_request import auth_passwordreset_request
from auth_login import auth_login
from auth_register import auth_register
from data import *
import pytest


#invalid email
def test_auth_passwordreset_request1():

    #create a test account
    register = auth_register("hello@gmail.com", "password", "first", "last")
    
    #this will throw an exception as the email entered isnt a valid email
    with pytest.raises(ValueError, match = '*Invalid Email Address*'):
        auth_passwordreset_request("Hellogmail.com")
        
#email not registered
def test_auth_passwordreset_request2():

    #assumes an account for the email address doesnt exist
    #register = testRegister("hello@gmail.com", "password", "first", "last")
    
    #this throws an error as the email is not belonging to a register user
    with pytest.raises(ValueError, match = '*Email doesnt Exists*'):
       auth_passwordreset_request("hello123@gmail.com")
        

