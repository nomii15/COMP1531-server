import pytest

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
    
def test_channel_messages_valueerror1():
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
        
    #ensure that two channel id are not same
    Channelid2 = Channelid + 1    
    #test part
    #channel with Channelid2 does not exist
    with pytest.raises(ValueError, match=r"*"):
        channel_messages(token1, Channelid2, 0)
        
def test_channel_message_valueerror2():
    #setup part
    authRegDict1 = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token1 = authRegDic1['token']
    Uid1 = authRegDic1['u_id']
    
    authRegDict2 = auth_register("Sad@gmail.com","qwe123","Sad","Woman")
    Uid2 = authRegDic2['u_id']
    
    Channelid = channels_create(token1, channel1, True)
    channel_invite(token1, Channelid, Uid2)
    
    for i in range(25):
        message_send(token1, Channelid, "hello")
        

    #test part
    #start is greater than the total number of messages in the channel
    with pytest.raises(ValueError, match=r"*"):
        channel_messages(token1, Channelid, 50)
        
def test_channel_message_accesserror():
    #setup part
    authRegDict1 = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token1 = authRegDic1['token']
    Uid1 = authRegDic1['u_id']
    
    authRegDict2 = auth_register("Sad@gmail.com","qwe123","Sad","Woman")
    token2 = authRegDic2['token']
    Uid2 = authRegDic2['u_id']
    
    Channelid = channels_create(token2, channel1, True)
    
    #test part
    #token1 user is not a member of channel with Channelid
    with pytest.raises(AccessError, match=r"*"):
        channel_messages(token1, Channelid, 0)
