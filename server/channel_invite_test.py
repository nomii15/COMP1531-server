import pytest

def test_channel_invite_correct_private():
    #setup part
    authRegDict1 = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token1 = authRegDic1['token']
       
    authRegDict2 = auth_register("Sad@gmail.com","qwe123","Sad","Woman")
    Uid2 = authRegDic2['u_id']  
    #create a private channel  
    Channelid = channels_create(token1, channel1, False)
    
    #test part
    channel_invite(token1, Channelid, Uid2)
    ChannelDic = channel_details(token1, Channelid)
    #whether user2 is in the channel
    assert(ChannelDic['all_members'][1]) == {'u_id': Uid2, 'name_first': 'Sad', 'name_last': 'Woman'}
    
    
def test_channel_invite_correct_public():
    #setup part
    authRegDict1 = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token1 = authRegDic1['token']
       
    authRegDict2 = auth_register("Sad@gmail.com","qwe123","Sad","Woman")
    Uid2 = authRegDic2['u_id']  
    #create a public channel  
    Channelid = channels_create(token1, channel1, True)
    
    #test part
    channel_invite(token1, Channelid, Uid2)
    ChannelDic = channel_details(token1, Channelid)
    #whether user2 is in the channel
    assert(ChannelDic['all_members'][1]) == {'u_id': Uid2, 'name_first': 'Sad', 'name_last': 'Woman'}
    
    
def test_channel_invite_invalid_channel():
    #setup part
    authRegDict1 = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token1 = authRegDic1['token']
    
    authRegDict2 = auth_register("Sad@gmail.com","qwe123","Sad","Woman")
    Uid2 = authRegDic2['u_id']
    
    authRegDict3 = auth_register("Saddd@gmail.com","qwe123","Saddd","Womannn")
    token3 = authRegDic3['token']
    
    Channelid1 = channels_create(token1, channel1, True)
    Channelid2 = channels_create(token3, channel2, True)
    
    #test part
    #user with token1 is not a authorised user in channel2
    with pytest.raises(ValueError, match=r"*"):
        channel_invite(token1, channel2, Uid2)
               
def test_channel_invite_invalid_user():
    #setup part
    authRegDict1 = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token1 = authRegDic1['token']
    
    Channelid1 = channels_create(token1, channel1, True)
    #test part
    #u_id is invalid(assume 999999999 is an invalid u_id)
    with pytest.raises(ValueError, match=r"*"):
        channel_invite(token1, channel1, 999999999)           
