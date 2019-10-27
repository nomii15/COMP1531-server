from auth_passwordreset_reset import auth_passwordreset_reset
import pytest

from auth_register_test import testRegister

class testReset():
    def __init__(self, code):
        self.code = code
    def codeCheck(self,code):
        if self.code != code:
            raise ValueError("Incorrect Reset Code")
        return True
    def passwordTest(self, pas):
        if len(pas) < 5:
            raise ValueError("Invalid Password Length")




#invalid reset code
def test_auth_passwordreset_reset1():
    
    #create a test account
    test = testRegister("z5110036@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz")
    
    testR = testReset("AB133")

    #assuming that the code from the email was "WER123"
    
    #this should not work as the code "ABS124" doesnt match "WER123"
    with pytest.raises(ValueError, match='*Incorrect Reset Code*'):
        testR.codeCheck("hello")
        
#invalid password
def test_auth_passwordreset_reset2():

    #create a test account
    test = testRegister("z5110036@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz")
    
    testR = testReset("AB133")
    
    if testR.codeCheck("AB133"):    
        #these should not work as the new passowrd lengths are <5
        with pytest.raises(ValueError, match='*Invalid Password Length*'):
                testR.passwordTest("pas")
        
#valid case
def test_auth_passwordreset_reset3():
    
    #create a test account
    test = testRegister("z5110036@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz")
    
    testR = testReset("AB133")
    
    if testR.codeCheck("AB133"):    
        testR.passwordTest("password")
        test.changepass("password")    
        #test to see if password updated
        assert test.password == "password"
        #this sequence should successfully reset the password
                   
