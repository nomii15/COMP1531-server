import pytest
import jwt
from auth_register import auth_register
from channels_create import channels_create
from channel_details import channel_details
from channel_invite import channel_invite
from data import *

SECRET = getSecret()

def test_channel_invite_success():
    auth_register('user1@gmail.com', 'qwe12345', 'user1', 'Zhang')
    auth_register('user2@gmail.com', 'secret123', 'user2', 'Happy')
    auth_register('user3@gmail.com', 'thisissecret123', 'user3', 'Sad')
    auth_register('user4@gmail.com', 'secretsecret123', 'user4', 'Good')    
    token1 = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    #unused token could be removed
    token2 = jwt.encode({'u_id': 2}, SECRET, algorithm='HS256').decode('utf-8')
    token3 = jwt.encode({'u_id': 3}, SECRET, algorithm='HS256').decode('utf-8')

    channel = channels_create(token1, 'ch1', True)
    channel_id = channel['channel_id']
    assert channel_details(token1, channel_id) == {'name': 'ch1', 'owner_members': [{'u_id': 1, 'name_first': 'user1', 'name_last': 'Zhang', 'profile_img_url': None}], 'all_members': [{'u_id': 1, 'name_first': 'user1', 'name_last': 'Zhang', 'profile_img_url': None}]}
    
    channel_invite(token1, channel_id, 2)
    assert channel_details(token1, channel_id) == {'name': 'ch1', 'owner_members': [{'u_id': 1, 'name_first': 'user1', 'name_last': 'Zhang', 'profile_img_url': None}], 'all_members': [{'u_id': 1, 'name_first': 'user1', 'name_last': 'Zhang', 'profile_img_url': None}, {'u_id': 2, 'name_first': 'user2', 'name_last': 'Happy', 'profile_img_url': None}]}

    channel_invite(token1, channel_id, 3)
    assert channel_details(token1, channel_id) == {'name': 'ch1', 'owner_members': [{'u_id': 1, 'name_first': 'user1', 'name_last': 'Zhang', 'profile_img_url': None}], 'all_members': [{'u_id': 1, 'name_first': 'user1', 'name_last': 'Zhang', 'profile_img_url': None}, {'u_id': 2, 'name_first': 'user2', 'name_last': 'Happy', 'profile_img_url': None}, {'u_id': 3, 'name_first': 'user3', 'name_last': 'Sad', 'profile_img_url': None}]}

def test_channel_invite_invalid_uid():
    token1 = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    with pytest.raises(ValueError, match='invalid u_id.'):
        channel_invite(token1, 1, 5)

def test_channel_invite_invalid_member():
    token4 = jwt.encode({'u_id': 4}, SECRET, algorithm='HS256').decode('utf-8')
    with pytest.raises(AccessError, match='inviter is not a member of the given channel.'):
        channel_invite(token4, 1, 1)

def test_channel_invite_invalid_channelid():
    token1 = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    with pytest.raises(ValueError, match='invalid channel.'):
        channel_invite(token1, 100, 3)
        
