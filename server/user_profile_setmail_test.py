import pytest
import jwt

SECRET = 'COMP1531'

data = {
    'users':{
        '001':{'email': 'abcdefg@gmail.com', 'name_first': 'Tom', 'name_last': 'Happy', 'handle': 'tomhappy'},
        '002':{'email': 'qwerty@gmail.com', 'name_first': 'Bob', 'name_last': 'Sad', 'handle': 'bobsad'}
    }
}

class test_mail():
    def __init__(self, token, email):
        payload = jwt.decode(token, SECRET, algorithms=['HS256'])
        self.u_id = payload['u_id']
        self.email = email
        
    def email_check(self):
        return True
        
    def email_beenused(self):
        for key, item in data['users'].items():
            if item['email'] == self.email:
                raise ValueError("email been used")
        return True
    
    def change(self):
        data['users'][self.u_id]['email'] = self.email
        
    def new_data(self):
        return data['users'][self.u_id]

#success
def test_1():
    token = jwt.encode({'u_id': '001'}, SECRET, algorithm='HS256')
    test1 = test_mail(token, 'abcdef@gmail.com')
    assert test1.email_check() == True
    assert test1.email_beenused() == True
    test1.change()
    assert test1.new_data() == {'email': 'abcdef@gmail.com', 'name_first': 'Tom', 'name_last': 'Happy', 'handle': 'tomhappy'}
    
#email has been used
def test_2():
    token = jwt.encode({'u_id': '001'}, SECRET, algorithm='HS256')
    test2 = test_mail(token, 'qwerty@gmail.com')
    with pytest.raises(ValueError, match='*email been used*'):
        test2.email_beenused()
