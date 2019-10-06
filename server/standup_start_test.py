from standup_start import standup_start
import pytest

#working setup
def test_standup_start1():
    
    #generate a token
    test_login = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
    
    token = test_login['token']
    
    #generate a channel
    channel = channels_create(token, "name", True)
    Id = channel['channel_id']
    
    #get the current time
    curr = datetime(2019,10,4,14,0)
    
    #send a message
    message_send(token, Id, "standup_send")
    
    #this should return the time in the form of datetime (for 15 min duration)
    time = standup_start(token, Id)
    
    #this test should pass as the time duration is 15 min
    assert time == (curr + time(14,15))
    
    
    
#invalid channel
def test_standup_start2():
    
    
    #generate a token
    test_login = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
    
    token = test_login['token']
    
    #generate a channel
    channel = channels_create(token, "name", True)
    Id = channel['channel_id']
    
    #assume the channel id isnt valid and the invalid channel id is passed in
    #send a message to the correct channel
    message_send(token, Id, "standup_send")
    
    #this should fail as an invalid channel id is passed
    #assume the channel id 13 doesnt match variable Id
    with pytest.raises(ValueError, match = '*Invalid Channel ID*'):
        standup_start("#11", 13)
        
        
#invalid token
def test_standup_start3():

    #generate a token
    test_login = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
   
    token = test_login['token']
    
    #generate a channel
    channel = channels_create(token, "name", True)
    Id = channel['channel_id']
    
    #send a message
    message_send(token, Id, "standup_send")
    
    #assume invalid token, such that token variable above is not the 
    #same as the token being passed in
    with pytest.raises(ValueError, match = '*Invalid Token*'):
        standup_start("#72", 3)
        
#not an authorised user
def test_standup_start4():
    
    #generate a token
    test_login = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
   
    token = test_login['token']
    
    #assume the channel is created and the user isnt a member
    
    #send a message
    message_send(token, Id, "standup_send")
    
    #this should fail as the user us not a member of the channel
    with pytest.raises(AccessError, match = '*Not a Member of the Channel*'):
        standup_start(token, 4)
    
    
    
    
    
                        

