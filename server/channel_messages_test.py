import pytest
from auth_register import auth_register
from channels_create import channels_create
from message_send import message_send
from channel_messages import channel_messages

from data import *


def test_channel_messages_correct():
    #setup part
    authRegDict1 = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token1 = authRegDict1['token']
    Uid1 = authRegDict1['u_id']
    
    Channelid = channels_create(token1, "name1", True)
    
  
    message_send(token1, Channelid['channel_id'], "hello")
    
    #test part    
    MessageDic = channel_messages(token1, Channelid['channel_id'], 0)
    assert(MessageDic['start']) == 0
    assert(MessageDic['end']) == -1

    for i in range(0,45):
        message_send(token1, Channelid['channel_id'], "hello")


    MessageDic = channel_messages(token1, Channelid['channel_id'], 40)
    assert(MessageDic['start']) == 40
    assert(MessageDic['end']) == -1
   


def test_channel_messages_valueerror1():

    #register
    test = auth_register("z5110046@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz")

    token1 = test['token']
    #create a channel
    chan = Channelid = channels_create(token1, "name1", True) 
       
    #test part
    #invalid channel id
    with pytest.raises(ValueError, match="Invalid Channel ID"):
        channel_messages(token1, 50,0)
        
def test_channel_message_valueerror2():
    #setup part
    #register
    test = auth_register("z5110056@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz")
    token1 = test['token']
    #create a channel
    chan = channels_create(token1, "name11", True)  
       

    #test part
    #start is greater than the total number of messages in the channel
    with pytest.raises(ValueError, match=r"*"):
        channel_messages(token1,chan['channel_id'] ,5)
        
def test_channel_message_accesserror():
    #setup part
    test1 = auth_register("z5110096@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz")
    token1 = test1['token']

    test2 = auth_register("z5110086@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz")
    token2 = test2['token']


    #create a channel
    chan = channels_create(token1, "name11", True)     
    
    #test part
    #token1 user is not a member of channel with Channelid
    with pytest.raises(AccessError, match=r"*"):
        channel_messages(token2,chan['channel_id'], 0)
