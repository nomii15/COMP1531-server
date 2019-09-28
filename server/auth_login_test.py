##auth login test file

from auth_login import *
import pytest

#checking for bad email addresses
def test_auth_login1():
    with pytest.raises(ValueError, match='*Invalid Email Address*'):
        auth_login("someemail53278.com", "hello123")
        auth_login("whatisthisemail.com", "hello123")
        
#checking for incorrect password
def test_auth_login2():
    with pytest.raises(ValueError, match='*Invalid Password*'):
        auth_login("z5110036@unsw.edu.au", "Trimesters")
        auth_login("z5160026@unsw.edu.au", "password")
            
#valid cases
def test_auth_login3():
    assert(auth_login("z5110036@unsw.edu.au", "Hello123") == "#")
    assert(auth_login("z5163179@unsw.edu.au", "Hello123") == "#")        
