from auth_passwordreset_reset import *
import pytest


#invalid reset code
def test_auth_passwordreset_reset1():
    with pytest.raises(ValueError, match='*Incorrect Reset Code*'):
        auth_passwordreset_reset("something", "ABS124")
        
#invalid password
def test_auth_passwordreset_reset2():
    with pytest.raises(ValueError, match='*Invalid Password Length*'):
        auth_passwordreset_reset("AUW624", "")
        auth_passwordreset_reset("AUW624", "nope")
        
#valid case
def test_auth_passwordreset_reset3():
    assert auth_passwordreset_reset("AUW624", "Valispass12") == "Password Reset" 
                   
