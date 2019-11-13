import pytest
import jwt
from auth_register import auth_register
from user_profile import user_profile
from data import *

SECRET = getSecret()

def test_user_profile_success():
    auth_register('qwe123@gmail.com', 'qwe12345', 'Vincent', 'Zhang')
    auth_register('abcdef@gmail.com', 'secret123', 'ABC', 'Happy')    
    token1 = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    token2 = jwt.encode({'u_id': 2}, SECRET, algorithm='HS256').decode('utf-8')
    assert user_profile(1, token1) == {'email': 'qwe123@gmail.com', 'name_first': 'Vincent', 'name_last': 'Zhang', 'handle_str': 'vincentzhang1', 'profile_img_url': None}
    assert user_profile(2, token1) == {'email': 'abcdef@gmail.com', 'name_first': 'ABC', 'name_last': 'Happy', 'handle_str': 'abchappy2', 'profile_img_url': None}
    assert user_profile(1, token2) == {'email': 'qwe123@gmail.com', 'name_first': 'Vincent', 'name_last': 'Zhang', 'handle_str': 'vincentzhang1', 'profile_img_url': None}

def test_user_profile_invalidtoken():
    token = jwt.encode({'u_id': 3}, SECRET, algorithm='HS256').decode('utf-8')
    assert user_profile(1, token) == {'error' : 'invalid token'}
    
def test_user_profile_invalid_uid():
    token = jwt.encode({'u_id': 1}, SECRET, algorithm='HS256').decode('utf-8')
    with pytest.raises(ValueError, match='invalid u_id'):
        user_profile(3, token)
