import pytest
import jwt
from auth_register import auth_register
from user_profile import user_profile
from user_profile_setmail import user_profile_setmail
from data import *

SECRET = getSecret()

def test_setmail_success():
    auth_register('qwe123@gmail.com', 'qwe12345', 'Vincent', 'Zhang')
    auth_register('abcdef@gmail.com', 'secret123', 'ABC', 'Happy')    
    token1 = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    token2 = jwt.encode({'u_id': 2}, SECRET, algorithm='HS256').decode('utf-8')
    user_profile_setmail(token1, 'qwert123@gmail.com')
    user_profile_setmail(token2, 'qwertyuiop@gmail.com')
    assert user_profile(1,token1,) == {'email': 'qwert123@gmail.com', 'name_first': 'Vincent', 'name_last': 'Zhang', 'handle_str': 'vincentzhang1', 'profile_img_url': None}
    assert user_profile(2,token1,) == {'email': 'qwertyuiop@gmail.com', 'name_first': 'ABC', 'name_last': 'Happy', 'handle_str': 'abchappy2', 'profile_img_url': None}

def test_setmail_invalid_token():
    token = jwt.encode({'u_id': 3}, SECRET, algorithm='HS256').decode('utf-8')
    assert user_profile_setmail(token, 'abc@gmail.com') == {'error' : 'invalid token'}
    
def test_setmail_invalid_email():
    token1 = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    token2 = jwt.encode({'u_id': 2}, SECRET, algorithm='HS256').decode('utf-8')
    with pytest.raises(ValueError, match='Invalid email address'):
        user_profile_setmail(token1, 'qwert123')
        user_profile_setmail(token2, 'qwertyuiop@.com')
        
def test_setmail_used():
    token1 = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    token2 = jwt.encode({'u_id': 2}, SECRET, algorithm='HS256').decode('utf-8')
    with pytest.raises(ValueError, match='email address has been used'):
        user_profile_setmail(token1, 'qwert123@gmail.com')
        
