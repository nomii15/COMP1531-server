import pytest

def test_channel_details_correct():
    #setup part  
    authRegDict1 = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token1 = authRegDic1['token']
    Uid1 = authRegDic1['u_id']
    
    authRegDict2 = auth_register("Sad@gmail.com","qwe123","Sad","Woman")
    Uid2 = authRegDic2['u_id']
    
    Channelid = channels_create(token1, channel1, True)
    channel_invite(token1, Channelid, Uid2)    
    #test part    
    ChannelDic = channel_details(token1, Channelid)

    assert(ChannelDic['name']) == 'channel1'
    assert(ChannelDic['owner_members'][0]) == {'u_id': Uid1, 'name_first': 'Happy', 'name_last': 'Man'}
    assert(ChannelDic['all_members'][0]) == {'u_id': Uid1, 'name_first': 'Happy', 'name_last': 'Man'}
    assert(ChannelDic['all_members'][1]) == {'u_id': Uid2, 'name_first': 'Sad', 'name_last': 'Woman'}
    
def test_channel_details_valueerror():
    #setup part
    authRegDict1 = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token1 = authRegDic1['token']
    #test part
    #channel id does not exist   
    with pytest.raises(ValueError, match=r"*"):
        channel_details(token1, 123)
        
def test_channel_details_accesserroe():
    #setup part
    authRegDict1 = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token1 = authRegDic1['token']
    
    authRegDict2 = auth_register("Sad@gmail.com","qwe123","Sad","Woman")
    token2 = authRegDic2['token']
    
    Channelid = channels_create(token2, channel1, True)
    #test part
    #user with token1 is not a member of channel 1
    with pytest.raises(AccessError, match=r"*"):
        channel_details(token1, Channelid)


