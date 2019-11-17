from search import Search_function
from auth_register import auth_register
from channels_create import channels_create
from message_send import message_send
from data import *

from hypothesis import given, example
from hypothesis.strategies import text

import pytest

#valid case where the user send a message and it checks to see if the messge is there
def test_search1():
    
    #generate a test login
    register = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
    
    #get the token
    token = register['token']
    u_id = register['u_id']

    #send a message in a channel that the user is in
    channel_id = channels_create(token, "this channel", True)
    message_id = message_send(token, channel_id['channel_id'], "Hello")

    query = "Hello"
    #this should return a collection of message that 
    #contain or partially the string "Hello"
    messages = Search_function(token, query)

    #test to see if the query string used found messages in channels
    #even if the message is a prefix of the query string
    for i in messages['messages']:
        assert i['message'] == "Hello"
    
#invalid token    
def test_search2():

    # using the setup in test1, if a users attamps to search without a valid token
    # throw exception, querty = Hello
    falseToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoyfQ.2QcZ_q4JJoHF-NQC1qWnsEcuPElVzN8T44LQgr-UyNo'
    with pytest.raises(ValueError, match = '*Invalid Token*'):
        Search_function(falseToken, "Hello")
        
        
        
#search for a message > 1000 characters  
def test_search3():

    #using the setup from the first test, 
    # attempt to search for a message that is greater than 1000 characters
    message = "A"*1001

    #generate a test login
    register = auth_register("z5110066@unsw.edu.au", "1234567", "John", "Smith")
    
    #get the token
    token = register['token']
    u_id = register['u_id']
    
    #this should fail as the message being looked for is > 1000 characters
    with pytest.raises(ValueError, match = '*Invalid Message Length*'):
        Search_function(token, message)

# if generating a random string and search for it, it shouldnt be there
@given(text())
def test_search_auto(string):
    #generate a token
    global SECRET
    SECRET = getSecret()
    token = jwt.encode({'u_id':1}, SECRET, algorithm='HS256').decode('utf-8')

    return_message = Search_function(token, string)
    i = False
    for j, item in return_message.items():
        if item['message'] == string:
            i = True
    #it gets through searching the messages and doesnt find anything, i is false
    assert i==False 

