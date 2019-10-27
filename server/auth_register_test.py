from auth_register import register
import pytest
from email_check import email_check

'''
(email, password, name_first, name_last)
{ u_id, token }
'''

from json import dumps
import jwt

class testRegister():
    def __init__(self,email,password,name_first,name_last):
        self.email = email
        self.password = password
        self.name_first = name_first
        self.name_last = name_last
        self.u_id = 0
    def emailTest(self):
        if email_check(self.email)=="Invalid Email":
            raise ValueError("Invalid Email Address")
    def passwordTest(self):
        if len(self.password) < 5:
            raise ValueError("Invalid Password Length")
    def nameFirst(self):
        if len(self.name_first) > 50 or len(self.name_first) == 0:
            raise ValueError("Invalid First Name Length")
    def nameLast(self):
        if len(self.name_last) > 50 or len(self.name_last) == 0:
            raise ValueError("Invalid Last Name Length")
    def valid(self):
        SECRET = 'comp1531'
        return {'u_id': self.u_id, 'token': jwt.encode({'u_id':self.u_id}, SECRET, algorithm='HS256').decode('utf-8')}			




def test_auth():
    
    test = testRegister("thisemaildoesntwork.com", "none0", "Fred", "Murry")

    with pytest.raises(ValueError, match='*Invalid Email Address*'):
        test.emailTest()


def test_auth_register1():
    #these tests will not work as the email is not valid

    
    test1 = testRegister("thiedwwork.com", "none", "Fred", "Murry")
    test2 = testRegister("notvalid.com", "12324545", "Some", "Name")
    test3 = testRegister("", "12324545", "Some", "Name")

    with pytest.raises(ValueError, match='*Invalid Email Address*'):
        test1.emailTest()
        test1.emailTest()
        test1.emailTest()

'''
#test existing email
def test_auth_register2():
    
    #sample register 
     test1 = testRegister("z5160026@unsw.edu.au", "hello123", "Some", "Name")    
    
    #this should raise an error as the email being used to register
    #already has been used to create an account 
    with pytest.raises(ValueError, match='*Email Already Exists*'):
        auth_register("z5160026@unsw.edu.au", "none5", "Fred", "Murry")      
'''       
#invalid password length        
def test_auth_register3():
    #should raise error as the password lengths used are <5
    test1 = testRegister("z5110036@unsw.edu.au", "hi", "Anne", "Smith")
    test2 = testRegister("z5260026@unsw.edu.au", "this", "A", "Name")
    test3 = testRegister("z5110036@unsw.edu.au", "", "Some", "Name")
    
    with pytest.raises(ValueError, match='*Invalid Password Length*'):
        test1.passwordTest()
        test2.passwordTest()
        test3.passwordTest()

#invalid first name length        
def test_auth_register4():
    #should not work as the first name lengths are >50 or =0
    test1 = testRegister("z5110036@unsw.edu.au", "password", "hsnrentjhfhdhgxbdsbdehbrewfjreaihdvayuefyugwefqhbr54jnkgfiuh", "Smith")
    test2 = testRegister("z5260026@unsw.edu.au", "SomE32476", "", "Name")

    with pytest.raises(ValueError, match='*Invalid First Name Length*'):
        test1.nameFirst()
        test2.nameFirst()
        

#invalid last name length        
def test_auth_register5():
    #should not work as the first name lengths are >50 or =0  
    test1 = testRegister("z5110036@unsw.edu.au", "password", "Martin", "hsnrentjhfhdhgxbdsbdehbrewfjreaihdvayuefyugwefqhbr54jnkgfiugfdsh")
    test2 = testRegister("z5260026@unsw.edu.au", "SomE32476", "First", "")      
    
    with pytest.raises(ValueError, match='*Invalid Last Name Length*'):
        test1.nameLast()
        test2.nameLast()
        

#valid
def test_auth_register6():
    #this case should successfully create an account and return and     
    #valid u_id and token, this example return a dummy id and token
    SECRET = 'comp1531'
    
    test = testRegister("z5110036@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz")
    test.emailTest()
    test.passwordTest()
    test.nameFirst()
    test.nameLast() 
    assert test.valid() == {'u_id': test.u_id, 'token': jwt.encode({'u_id':test.u_id}, SECRET, algorithm='HS256').decode('utf-8')}      
        
