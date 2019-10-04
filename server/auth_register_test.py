from auth_register import *
import pytest

'''
(email, password, name_first, name_last)
{ u_id, token }
'''

#test invalid email
def test_auth_register1():
    #these tests will not work as the email is not valid  
    
    with pytest.raises(ValueError, match='*Invalid Email Address*'):
        auth_register("thisemaildoesntwork.com", "none", "Fred", "Murry")
        auth_register("notvalid.com", "12324545", "Some", "Name")
        auth_register("", "12324545", "Some", "Name")
        
#test existing email
def test_auth_register1():
    
    #sample register 
    register = auth_register("z5160026@unsw.edu.au", "hello123", "Some", "Name")    
    
    #this should raise an error as the email being used to register
    #already has been used to create an account 
    with pytest.raises(ValueError, match='*Email Already Exists*'):
        auth_register("z5160026@unsw.edu.au", "none5", "Fred", "Murry")      
        
#invalid password length        
def test_auth_register2():
    #should raise error as the password lengths used are <5    
    
    with pytest.raises(ValueError, match='*Invalid Password Length*'):
        auth_register("z5110036@unsw.edu.au", "hi", "Anne", "Smith")
        auth_register("z5260026@unsw.edu.au", "this", "A", "Name")
        auth_register("z5110036@unsw.edu.au", "", "Some", "Name")

#invalid first name length        
def test_auth_register3():
    #should not work as the first name lengths are >50 or =0

    with pytest.raises(ValueError, match='*Invalid First Name Length*'):
        auth_register("z5110036@unsw.edu.au", "password", "hsnrentjhfhdhgxbdsbdehbrewfjreaihdvayuefyugwefqhbr54jnkgfiuh", "Smith")
        auth_register("z5260026@unsw.edu.au", "SomE32476", "", "Name")
        

#invalid last name length        
def test_auth_register4():
    #should not work as the first name lengths are >50 or =0        
    
    with pytest.raises(ValueError, match='*Invalid Last Name Length*'):
        auth_register("z5110036@unsw.edu.au", "password", "Martin", "hsnrentjhfhdhgxbdsbdehbrewfjreaihdvayuefyugwefqhbr54jnkgfiugfdsh")
        auth_register("z5260026@unsw.edu.au", "SomE32476", "First", "")
        

#valid
def test_auth_register5():
    #this case should successfully create an account and return and     
    #valid u_id and token, this example return a dummy id and token
    
    assert auth_register("z5110036@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz") == {0, "#"}             
        
                            
