import pytest
import jwt
from auth_register import auth_register
from user_profile import user_profile
from user_profile_setname import user_profile_setname
from data import *

SECRET = getSecret()

def test_setname_success():
    auth_register('qwe123@gmail.com', 'qwe12345', 'Vincent', 'Zhang')
    auth_register('abcdef@gmail.com', 'secret123', 'ABC', 'Happy')    
    token1 = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    token2 = jwt.encode({'u_id': 2}, SECRET, algorithm='HS256').decode('utf-8')
    user_profile_setname(token1, 'ABC', 'Sad')
    user_profile_setname(token2, 'hahaha', 'happyhappy')
    user_profile_setname(token2, 'ABCDEF', 'Happy')
    assert user_profile(1, token1) == {'email': 'qwe123@gmail.com', 'name_first': 'ABC', 'name_last': 'Sad', 'handle_str': 'vincentzhang1', 'profile_img_url': None}
    assert user_profile(2, token1) == {'email': 'abcdef@gmail.com', 'name_first': 'ABCDEF', 'name_last': 'Happy', 'handle_str': 'abchappy2', 'profile_img_url': None}
    
def test_setname_invalid_token():
    token = jwt.encode({'u_id': 3}, SECRET, algorithm='HS256').decode('utf-8')
    assert user_profile_setname(token, 'abc', 'happy') == {'error' : 'invalid token'}
    
def test_setname_incorrect_firstlen():
    token = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    with pytest.raises(ValueError, match='incorrect first name length'):
        user_profile_setname(token, '', 'happy')
        user_profile_setname(token, 'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm', 'happy')
        
def test_setname_incorrect_lastlen():
    token = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    with pytest.raises(ValueError, match='incorrect last name length'):
        user_profile_setname(token, 'abc', '')
        user_profile_setname(token, 'abc' 'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm')
