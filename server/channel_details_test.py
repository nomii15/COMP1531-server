import pytest
import jwt

SECRET = 'COMP1531'

data = {
    'channel_details':{
        '1':{'name': 'channel1', 'all_members': ['001','002']},
        '2':{'name': 'channel1', 'all_members': ['003','004']}
    }
}

class test_detail():
    def __init__(self, token, channel_id):
        self.channel_id = channel_id
        payload = jwt.decode(token, SECRET, algorithms=['HS256'])
        self.u_id = payload['u_id']
        
    def id_check(self):
        for key, item in data['channel_details'].items():
            if key == self.channel_id:
                return True
        raise ValueError("invalid channel_id")
        
    def member_check(self):
        for member in data['channel_details'][self.channel_id]['all_members']:
            if member == self.u_id:
                return True
        raise AccessError("not a member of the channel")
        
    def success(self):
        return data['channel_details'][self.channel_id]

#return information about channel 1
def test_1():
    token = jwt.encode({'u_id': '001'}, SECRET, algorithm='HS256')
    test1 = test_detail(token, '1')
    assert test1.id_check() == True
    assert test1.member_check() == True
    assert test1.success() == {'name': 'channel1', 'all_members': ['001', '002']}

#invalid channel_id
def test_2():
    token = jwt.encode({'u_id': '001'}, SECRET, algorithm='HS256')
    test2 = test_detail(token, '3')
    with pytest.raises(ValueError, match='*invalid channel_id*'):
        test2.id_check()

#not a member of the channel
def test_3():
    token = jwt.encode({'u_id': '003'}, SECRET, algorithm='HS256')
    test3 = test_detail(token, '1')
    with pytest.raises(AccessError, match='*not a member of the channel*'):
        test2.member_check()
