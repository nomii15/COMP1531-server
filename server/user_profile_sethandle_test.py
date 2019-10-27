import pytest
import jwt

SECRET = 'COMP1531'

data = {
    'users':{
        '001':{'email': 'abcdefg@gmail.com', 'name_first': 'Tom', 'name_last': 'Happy', 'handle': 'tomhappy'},
        '002':{'email': 'qwerty@gmail.com', 'name_first': 'Bob', 'name_last': 'Sad', 'handle': 'bobsad'}
    }
}

class test_handle():
    def __init__(self, token, handle):
        payload = jwt.decode(token, SECRET, algorithms=['HS256'])
        self.u_id = payload['u_id']
        self.handle = handle
        
    def handle_length(self):
        if 3 <= len(self.handle) <= 20:
            return True
        raise ValueError("incorrect length")
        
    def handle_check(self):
        for key, item in data['users'].items():
            if item['handle'] == self.handle:
                raise ValueError("handle been used")
        return True
    
    def change(self):
        data['users'][self.u_id]['handle'] = self.handle
        
    def new_data(self):
        return data['users'][self.u_id]

#success
def test_1():
    token = jwt.encode({'u_id': '001'}, SECRET, algorithm='HS256')
    test1 = test_handle(token, 'abcdef')
    assert test1.handle_length() == True
    assert test1.handle_check() == True
    test1.change()
    assert test1.new_data() == {'email': 'abcdefg@gmail.com', 'name_first': 'Tom', 'name_last': 'Happy', 'handle': 'abcdef'}
    
#incorrect length
def test_2():
    token = jwt.encode({'u_id': '001'}, SECRET, algorithm='HS256')
    test2 = test_name(token, 'a')
    with pytest.raises(ValueError, match='*incorrect length*'):
        test2.handle_length()

#handle been used
def test_3():
    token = jwt.encode({'u_id': '001'}, SECRET, algorithm='HS256')
    test3 = test_name(token, 'bobsad')
    with pytest.raises(ValueError, match='*handle been used*'):
        test3.handle_check()
