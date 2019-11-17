import pytest
import jwt
from auth_register import auth_register
from channels_create import channels_create
from channel_details import channel_details
from channel_invite import channel_invite
#import Error.py
from data import *


SECRET = getSecret()

def test_channel_details_success():
    auth_register('qwe123@gmail.com', 'qwe12345', 'Vincent', 'Zhang')
    auth_register('abcdef@gmail.com', 'secret123', 'ABC', 'Happy')    
    token1 = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    #unused token could be removed
    token2 = jwt.encode({'u_id': 2}, SECRET, algorithm='HS256').decode('utf-8')
    channel = channels_create(token1, 'ch1', True)
    channel_id = channel['channel_id']
    assert channel_details(token1, channel_id) == {'name': 'ch1', 'owner_members': [{'u_id': 1, 'name_first': 'Vincent', 'name_last': 'Zhang', 'profile_img_url': None}], 'all_members': [{'u_id': 1, 'name_first': 'Vincent', 'name_last': 'Zhang', 'profile_img_url': None}]}

    channel_invite(token1, channel_id, 2)
    assert channel_details(token1, channel_id) == {'name': 'ch1', 'owner_members': [{'u_id': 1, 'name_first': 'Vincent', 'name_last': 'Zhang', 'profile_img_url': None}], 'all_members': [{'u_id': 1, 'name_first': 'Vincent', 'name_last': 'Zhang', 'profile_img_url': None}, {'u_id': 2, 'name_first': 'ABC', 'name_last': 'Happy', 'profile_img_url': None}]}

    assert channel_details(token2, channel_id) == {'name': 'ch1', 'owner_members': [{'u_id': 1, 'name_first': 'Vincent', 'name_last': 'Zhang', 'profile_img_url': None}], 'all_members': [{'u_id': 1, 'name_first': 'Vincent', 'name_last': 'Zhang', 'profile_img_url': None}, {'u_id': 2, 'name_first': 'ABC', 'name_last': 'Happy', 'profile_img_url': None}]}

def test_channel_details_invalid_channelid():
    token1 = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    with pytest.raises(ValueError, match='Invalid channel_id'):
        channel_details(token1, 100)


def test_channel_details_invalid_member():
    auth_register('user3@gmail.com', 'secret12345', 'User', '3') 
    token3 = jwt.encode({'u_id': 3}, SECRET, algorithm='HS256').decode('utf-8')
    with pytest.raises(AccessError, match='Authorised user is not a member of this channel.'):
        channel_details(token3, 1)

