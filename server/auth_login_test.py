##auth login test file
from auth_login import auth_login
from auth_register import auth_register
import pytest
from data import *

#checking for bad email addresses
def test_auth_login1():

    #create a temp account
    register = auth_register("z5160026@unsw.edu.au", "hello123", "Some", "Name")
    
    #this will not work as the email typed in isnt a valid email and 
    #doesnt match the one they used to sign up with
    with pytest.raises(ValueError, match='*Invalid Email Address*'):
        auth_login("z5160026@unsw.au", "hello123")
        
#checking for incorrect password
def test_auth_login2():

    #create a temp account
    register = auth_register("z5110036@unsw.edu.au", "hello123", "Luke", "Smith")
    
    #this wont work as an incorrect password is typed in
    #Trimesters != hello123
    with pytest.raises(ValueError, match='*Invalid Password*'):
        auth_login("z5110036@unsw.edu.au", "Trimesters")
            
#valid cases
def test_auth_login3():
    
    #create a temp account
    register = auth_register("z5110066@unsw.edu.au", "hello123", "Daniel", "Setkiewicz")
    
    #which should work, but with a proper token and not a dummy one
    assert(auth_login("z5110066@unsw.edu.au", "hello123") == {'u_id': 3, 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjozfQ.qgB37wE5eljzo8PI7QPUJxbJEpuu0bTxT_oNPU7uEUo'})
           
