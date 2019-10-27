import pytest
import jwt

SECRET = 'COMP1531'

data = {
    'users':{
        '001':{'email': 'abcdefg@gmail.com', 'name_first': 'Tom', 'name_last': 'Happy', 'handle': 'tomhappy'},
        '002':{'email': 'qwerty@gmail.com', 'name_first': 'Bob', 'name_last': 'Sad', 'handle': 'bobsad'}
    }
}

class test_name():
    def __init__(self, token, name_first, name_last):
        payload = jwt.decode(token, SECRET, algorithms=['HS256'])
        self.u_id = payload['u_id']
        self.name_first = name_first
        self.name_last = name_last
        
    def first_check(self):
        if 1 <= len(self.name_first) <= 50:
            return True
        raise ValueError("incorrect length")
        
    def last_check(self):
        if 1 <= len(self.name_last) <= 50:
            return True
        raise ValueError("incorrect length")
        
    def change(self):
        data['users'][self.u_id]['name_first'] = self.name_first
        data['users'][self.u_id]['name_last'] = self.name_last
        
    def new_data(self):
        return data['users'][self.u_id]

#success
def test_1():
    token = jwt.encode({'u_id': '001'}, SECRET, algorithm='HS256')
    test1 = test_name(token, 'abc', '123')
    assert test1.first_check() == True
    assert test1.last_check() == True
    test1.change()
    assert test1.new_data() == {'email': 'abcdefg@gmail.com', 'name_first': 'abc', 'name_last': '123', 'handle': 'tomhappy'}
    
#incorrect name
def test_2():
    token = jwt.encode({'u_id': '001'}, SECRET, algorithm='HS256')
    test2 = test_name(token, '', '123')
    with pytest.raises(ValueError, match='*incorrect length*'):
        test2.first_check()
