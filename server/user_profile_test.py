import pytest
        
data = {
    'users':{
        '001':{'email': 'abcdefg@gmail.com', 'name_first': 'Tom', 'name_last': 'Happy', 'handle': 'tomhappy'},
        '002':{'email': 'qwerty@gmail.com', 'name_first': 'Bob', 'name_last': 'Sad', 'handle': 'bobsad'}
    }
}

class test_profile():
    def __init__(self, token, u_id):
        self.token = token
        self.u_id = u_id
        
    def id_check(self):
        for key, item in data['users'].items():
            if key == self.u_id:
                return True
        raise ValueError("invalid u_id")
            
    def success(self):
        return data['users'][self.u_id]

#return information for user 001
def test_1():
    test1 = test_profile(12345, '001')
    assert test1.id_check() == True
    assert test1.success() == {'email': 'abcdefg@gmail.com', 'name_first': 'Tom', 'name_last': 'Happy', 'handle': 'tomhappy'}

#return information for user 002
def test_2():
    test2 = test_profile(54321, '002')
    assert test2.id_check() == True
    assert test2.success() == {'email': 'qwerty@gmail.com', 'name_first': 'Bob', 'name_last': 'Sad', 'handle': 'bobsad'}
    
#invalid u_id
def test_3():
    test3 = test_profile(23451, '003')
    with pytest.raises(ValueError, match='*invalid u_id*'):
        test3.id_check()
