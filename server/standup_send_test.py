from standup_send import standup_send
from standup_start import standup_start
from standup_active import standup_active
from auth_register import auth_register
from channels_create import channels_create
from message_send import message_send
from data import *
import jwt
import time
import pytest

#valid case
def test_standup_send1():
    #generate a token
    test_login = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
   
    token = test_login['token']
    
    message = "Hello"
    
    #generate a channel
    channel = channels_create(token, "name", True)
    Id = channel['channel_id']
    
    #send a message
    message_send(token, Id, "/standup 5")
    
    #standup start, this would be called within the message_send
    standup_start(token, Id, 5)
    
    #send a message to the queue
    standup_send(token, Id, message)
    
    #check the buffer for the message to see if operating correctly
    #assume the dictionary returned was dictionary
    for items in standup:
        if message in items['messages']:
            assert message in items['messages']
    
    #this sequence would successfully call the standup functions and record the message during that time period


#invalid channel id   
def test_standup_send2():
     #generate a token
    test_login = auth_register("z5110066@unsw.edu.au", "1234567", "John", "Smith")
   
    token = test_login['token']
    
    #generate a channel
    channel = channels_create(token, "name", True)
    Id = channel['channel_id']
    
    #send a message
    message_send(token, Id, "/standup 50")
    
     #standup start, this would be called within the message_send
    standup_start(token, Id,40)
    
    #assume the channel id passed into standup_send is invalid
    #3 != Id
    with pytest.raises(ValueError, match = '*Invalid Channel Id*'):
        standup_send(token, 500, "hello there")
        

#message is too long (>1000)        
def test_standup_send3():

     #generate a token
    test_login = auth_register("z5110096@unsw.edu.au", "1234567", "John", "Smith")
   
    token = test_login['token']
    
    #generate a channel
    channel = channels_create(token, "name", True)
    Id = channel['channel_id']
    
    #send a message
    message_send(token, Id, "standup_send")
    
    #standup start, this would be called within the message_send
    standup_start(token, Id, 1000)
    
    #assume message is over 1000 characters long
    message = "a"*1001
    
    with pytest.raises(ValueError, match = '*Messsage length > 1000*'):
        standup_send(token, Id, message)   


#not a member of the channel
def test_standup_send4():

    #generate a token
    test_login = auth_register("z5220036@unsw.edu.au", "1234567", "John", "Smith")
   
    token = test_login['token']

    #this should fail as the user trying to start the standup isnt
    #a member of the channel
    
    with pytest.raises(AccessError, match = '*Not a Member*'):
        standup_send(token, 1, "hello there") 
        

#standup start is not active        
def test_standup_send5():

    #generate a token
    test_login = auth_register("z5221036@unsw.edu.au", "1234567", "John", "Smith")
   
    token = test_login['token']
    
    #generate a channel
    channel = channels_create(token, "name", True)
    Id = channel['channel_id']
    
    #assume standup start is not active  
    
    #this should fail as the user trying to send to the startup buffer 
    #hasnt activated the standup session    
    with pytest.raises(ValueError, match = '*Standup not active*'):
        standup_send(token, Id, "hello there")
  
    
    
      
