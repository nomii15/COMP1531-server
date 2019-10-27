import pytest
from auth_register_test import testRegister
from Error import *

class channel():
    def __init__(self, i_d, name):
        self.id = i_d
        self.name = name
        self.users = [0]

    def checkID(self, code):
        if self.id != code:
            raise ValueError("Invalid Channel ID")
    def read(self, start, end):
        if start > end:
            raise ValueError("Invalid Channel ID")  
    def messages(self,user):
        if user not in self.users:
            raise AccessError("not a member")

'''
def test_channel_messages_correct():
    #setup part
    authRegDict1 = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token1 = authRegDic1['token']
    Uid1 = authRegDic1['u_id']
    
    authRegDict2 = auth_register("Sad@gmail.com","qwe123","Sad","Woman")
    Uid2 = authRegDic2['u_id']
    
    Channelid = channels_create(token1, channel1, True)
    channel_invite(token1, Channelid, Uid2)
    
    for i in range(75):
        message_send(token1, Channelid, "hello")
    
    #test part    
    MessageDic = channel_messages(token1, Channelid, 0)
    assert(MessageDic['start']) == 0
    assert(MessageDic['end']) == 49
    
    MessageDic = channel_messages(token1, Channelid, 50)
    assert(MessageDic['start']) == 50
    assert(MessageDic['end']) == -1
'''
def test_channel_messages_valueerror1():

    #register
    test = testRegister("z5110036@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz")

    #create a channel
    chan = channel(0, "channel_name") 
       
    #test part
    #invalid channel id
    with pytest.raises(ValueError, match="Invalid Channel ID"):
        chan.checkID(1)
        
def test_channel_message_valueerror2():
    #setup part
    #register
    test = testRegister("z5110036@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz")

    #create a channel
    chan = channel(0, "channel_name") 
       

    #test part
    #start is greater than the total number of messages in the channel
    with pytest.raises(ValueError, match=r"*"):
        chan.read(40,20)
        
def test_channel_message_accesserror():
    #setup part
    test1 = testRegister("z5110036@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz")
    info1 = test1.valid()
    
    test2 = testRegister("hello@gmail.com.au", "SomePassword", "hello", "there")
    info2 = test2.valid()
    
    chan = channel(0, "channel_name")
    
    #test part
    #token1 user is not a member of channel with Channelid
    with pytest.raises(AccessError, match=r"*"):
        chan.messages(1)
