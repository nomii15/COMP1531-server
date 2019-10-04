from standup_send import *
import pytest

#valid case
def test_standup_send1():
    #generate a token
    test_login = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
   
    token = test_login['token']
    
    #generate a channel
    channel = channels_create(token, "name", True)
    Id = channel['channel_id']
    
    #send a message
    message_send(token, Id, "standup_send")
    
    #standup start, this would be called within the message_send
    standup_start(token, Id)
    
    #send a message to the queue
    standup_send(token, Id, "hello")
    
    #this sequence would successfully call the standup functions and record the message during that time period


#invalid channel id   
def test_standup_send2():
     #generate a token
    test_login = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
   
    token = test_login['token']
    
    #generate a channel
    channel = channels_create(token, "name", True)
    Id = channel['channel_id']
    
    #send a message
    message_send(token, Id, "standup_send")
    
     #standup start, this would be called within the message_send
    standup_start(token, Id)
    
    #assume the channel id passed into standup_send is invalid
    #3 != Id
    with pytest.raises(ValueError, match = '*Invalid Channel Id*'):
        standup_send(token, 3, "hello there")
        

#message is too long (>1000)        
def test_standup_send3():

     #generate a token
    test_login = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
   
    token = test_login['token']
    
    #generate a channel
    channel = channels_create(token, "name", True)
    Id = channel['channel_id']
    
    #send a message
    message_send(token, Id, "standup_send")
    
    #standup start, this would be called within the message_send
    standup_start(token, Id)
    
    #assume message is over 1000 characters long
    message
    
    with pytest.raises(ValueError, match = '*Messsage length > 1000*'):
        standup_send(token, Id, message)   


#not a member of the channel
def test_standup_send4():

    #generate a token
    test_login = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
   
    token = test_login['token']
    
    #assume the channel is created but the user is not a member of it
    #with channel id 013
    
    #send a message
    message_send(token, 013, "standup_send")
    
    #standup start, this would be called within the message_send
    standup_start(token, 013)
    
    #this should fail as the user trying to start the standup isnt
    #a member of the channel
    
    with pytest.raises(AccessError, match = '*Not a Member*'):
        standup_send(token, 013, "hello there") 
        

#standup start is not active        
def test_standup_send5():

    #generate a token
    test_login = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
   
    token = test_login['token']
    
    #generate a channel
    channel = channels_create(token, "name", True)
    Id = channel['channel_id']
    
    #assume standup start is not active  
    
    #this should fail as the user trying to send to the startup buffer 
    #hasnt activated the standup session    
    with pytest.raises(AccessError, match = '*Standup not active*'):
        standup_send(token, Id, "hello there")
  
    
    
      
