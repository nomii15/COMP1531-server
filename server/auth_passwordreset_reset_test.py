from auth_passwordreset_reset import auth_passwordreset_reset
import pytest


#invalid reset code
def test_auth_passwordreset_reset1():
    
    #create a test account
    register = auth_register("Someemial@hotmail.com.au", "Hello123", "First", "Last")
    
    #call password reset request
    auth_passwordreset_request("Someemial@hotmail.com.au")
    
    #assuming that the code from the email was "WER123"
    
    #this should not work as the code "ABS124" doesnt match "WER123"
    with pytest.raises(ValueError, match='*Incorrect Reset Code*'):
        auth_passwordreset_reset("ABS124", "SomePass")
        
#invalid password
def test_auth_passwordreset_reset2():

    #create a test account
    register = auth_register("Someemial@hotmail.com.au", "Hello123", "First", "Last")
    
    #call password reset request
    auth_passwordreset_request("Someemial@hotmail.com.au")
    
    #assume that the code generated was "AUW624"
    
    #these should not work as the new passowrd lengths are <5
    with pytest.raises(ValueError, match='*Invalid Password Length*'):
        auth_passwordreset_reset("AUW624", "")
        auth_passwordreset_reset("AUW624", "nope")
        
#valid case
def test_auth_passwordreset_reset3():
    
    #create a test account
    register = auth_register("Someemial@hotmail.com.au", "Hello123", "First", "Last")
    
    #call password reset request
    auth_passwordreset_request("Someemial@hotmail.com.au")
    
    #assume that the code generated was "AUW624"
    auth_passwordreset_reset("AUW624", "Valispass12") 
    
    #test to see if password updated
    assert new_user_password == "Valispass12"
    #this sequence should successfully reset the password
                   
