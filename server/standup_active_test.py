from standup_active import standup_active
from standup_send import standup_send
from standup_start import standup_start
from auth_register import auth_register
from channels_create import channels_create
from message_send import message_send
from data import *
import jwt
import time
import pytest

#not a valid channel id
def test_standup_active1():
    test_login = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
   
    token = test_login['token']

    with pytest.raises(ValueError, match = '*Invalid Channel Id*'):
        standup_active(token, 500)

#not a valid token
def test_standup_active2():
    test_login = auth_register("z5110066@unsw.edu.au", "1234567", "John", "Smith")   
    token = test_login['token']

    #generate a fake token
    global SECRET
    SECRET = getSecret()
    tokenFalse = jwt.encode({'u_id':-1}, SECRET, algorithm='HS256').decode('utf-8')

    with pytest.raises(ValueError, match = '*Invalid Channel Id*'):
        standup_active(tokenFalse, 500)

#valid case
def test_standup_active3():
    test_login = auth_register("z5110096@unsw.edu.au", "1234567", "John", "Smith")   
    token = test_login['token']

    #create channel
    channel = channels_create(token, "name", True)
    Id = channel['channel_id']

    status = standup_active(token, Id)
    assert status['is_active'] == False

#valid case active
def test_standup_active4():
    test_login = auth_register("z5112096@unsw.edu.au", "1234567", "John", "Smith")   
    token = test_login['token']

    #create channel
    channel = channels_create(token, "aname", True)
    Id = channel['channel_id']

    status = standup_active(token, Id)
    end = standup_start(token, Id, 500)
    status = standup_active(token, Id)

    assert status['is_active'] == True