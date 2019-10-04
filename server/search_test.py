from search import *
import pytest

def test_search1():
    
    #generate a test login
    register = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
    
    #get the token
    token = register['token']
    
    #this should return a collection of message that 
    #contain or partially the string "Hello"
    dictionary{} = search(token, "Hello")
    
    
#invalid token    
def test_search2():

    #generate a test login
    register = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
    
    #get the token
    token = register['token']
    
    #assume token != "#72"
    #this should fail as the token passed is not a valid token
    with pytest.raises(ValueError, match = '*Invalid Token*'):
        search("#72", "Hello")
        
#search for a message > 1000 characters  
def test_search3():

    #generate a test login
    register = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
    
    #get the token
    token = register['token']
    
    #assume message > 1000 characters
    message
    
    #this should fail as the message being looked for is > 1000 characters
    with pytest.raises(ValueError, match = '*Invalid Message Length*'):
        search(token, message)            
