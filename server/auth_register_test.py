from auth_register import *
import pytest

'''
(email, password, name_first, name_last)
{ u_id, token }
'''

#test invalid email
def test_auth_register1():
    with pytest.raises(ValueError, match='*Invalid Email Address*'):
        auth_register("thisemaildoesntwork.com", "none", "Fred", "Murry")
        auth_register("notvalid.com", "12324545", "Some", "Name")
        auth_register("", "12324545", "Some", "Name")
        
#test existing email
def test_auth_register1():
    with pytest.raises(ValueError, match='*Email Already Exists*'):
        auth_register("z5160026@unsw.edu.au", "none", "Fred", "Murry")      
        
#invalid password length        
def test_auth_register2():
    with pytest.raises(ValueError, match='*Invalid Password Length*'):
        auth_register("z5110036@unsw.edu.au", "hi", "Anne", "Smith")
        auth_register("z5260026@unsw.edu.au", "this", "A", "Name")
        auth_register("z5110036@unsw.edu.au", "", "Some", "Name")

#invalid first name length        
def test_auth_register3():
    with pytest.raises(ValueError, match='*Invalid First Name Length*'):
        auth_register("z5110036@unsw.edu.au", "password", "hsnrentjhfhdhgxbdsbdehbrewfjreaihdvayuefyugwefqhbr54jnkgfiuh", "Smith")
        auth_register("z5260026@unsw.edu.au", "SomE32476", "", "Name")
        

#invalid last name length        
def test_auth_register4():
    with pytest.raises(ValueError, match='*Invalid Last Name Length*'):
        auth_register("z5110036@unsw.edu.au", "password", "Martin", "hsnrentjhfhdhgxbdsbdehbrewfjreaihdvayuefyugwefqhbr54jnkgfiugfdsh")
        auth_register("z5260026@unsw.edu.au", "SomE32476", "First", "")
        

#valid
def test_auth_register5():
    assert auth_register("z5110036@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz") == {0, "#"}             
        
                            
