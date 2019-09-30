import pytest
from auth_passwordreset_request import *


#invalid email
def test_auth_passwordreset_request1():
    with pytest.raises(ValueError, match = '*Invalid Email Address*'):
        auth_passwordreset_request("someemail.com")
        
#email not registered
def test_auth_passwordreset_request2():
    with pytest.raises(ValueError, match = '*Not a Registed Email Address*'):
        auth_passwordreset_request("z5260026@unsw.edu.au")
        
#valid
def test_auth_passwordreset_request3():
    assert auth_passwordreset_request("z5110036@unsw.edu.au") == "Sending Request"             
