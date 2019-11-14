import pytest
import jwt
from auth_register import auth_register
from user_profile import user_profile
from user_profile_sethandle import user_profile_sethandle
from data import *

SECRET = getSecret()

def test_sethandle_success():
    auth_register('qwe123@gmail.com', 'qwe12345', 'Vincent', 'Zhang')
    auth_register('abcdef@gmail.com', 'secret123', 'ABC', 'Happy')    
    token1 = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    token2 = jwt.encode({'u_id': 2}, SECRET, algorithm='HS256').decode('utf-8')
    user_profile_sethandle(token1, 'handle1')
    user_profile_sethandle(token2, 'handle2')
    user_profile_sethandle(token1, 'sup_handle')
    assert user_profile(1, token1) == {'email': 'qwe123@gmail.com', 'name_first': 'Vincent', 'name_last': 'Zhang', 'handle_str': 'sup_handle', 'profile_img_url': None}
    assert user_profile(2, token2) == {'email': 'abcdef@gmail.com', 'name_first': 'ABC', 'name_last': 'Happy', 'handle_str': 'handle2', 'profile_img_url': None}
    
def test_sethandle_invalid_token():
    token = jwt.encode({'u_id': 3}, SECRET, algorithm='HS256').decode('utf-8')
    assert user_profile_sethandle(token, 'handlehandle') == {'error' : 'invalid token'}
    
def test_sethandle_incorrect_len(): 
    token1 = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    token2 = jwt.encode({'u_id': 2}, SECRET, algorithm='HS256').decode('utf-8')
    with pytest.raises(ValueError, match='incorrect handle length'):
        user_profile_sethandle(token1, 'ab')
        user_profile_sethandle(token2, 'handlehandlehandlehandlehandle')
        
def test_sethandle_used():
    token = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    with pytest.raises(ValueError, match='handle has been used'):
        user_profile_sethandle(token, 'handle2')
