from search import search
from auth_register_test import testRegister
import pytest

class search():
    def __init__(self,query,token):
        self.query = query
        self.token = token
    def tokencheck(self, token):
        if self.token != token:
            raise ValueError("Invalid token")
    def messagetest(self):
        if len(self.query) > 1000:
            raise ValueError("Message too long")                    
    '''
def test_search1():
    
    #generate a test login
    register = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
    
    #get the token
    token = register['token']
    query = "Hello"
    #this should return a collection of message that 
    #contain or partially the string "Hello"
    dictionary{} = search(token, query)
    
    #test to see if the query string used found messages in channels
    #even if the message is a prefix of the query string
    
    assert query.startswith(query, 0,len(query)) in dictionary.items()
    '''
    
#invalid token    
def test_search2():

    #generate a test login
    register = testRegister("z5110036@unsw.edu.au", "1234567", "John", "Smith")
    test = search("hello there", 1)
    #get the token
    out = register.valid()
    
    #assume token != "#72"
    #this should fail as the token passed is not a valid token
    with pytest.raises(ValueError, match = '*Invalid Token*'):
        test.tokencheck(2)
        
        
#search for a message > 1000 characters  
def test_search3():

    #generate a test login
    register = testRegister("z5110036@unsw.edu.au", "1234567", "John", "Smith")
    message = 'S'*1001
    test = search(message, 1)
    #get the token
    out = register.valid()
    
    #this should fail as the message being looked for is > 1000 characters
    with pytest.raises(ValueError, match = '*Invalid Message Length*'):
        test.messagetest()            
