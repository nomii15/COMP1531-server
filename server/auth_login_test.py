##auth login test file

from auth_login import login
from auth_register_test import testRegister
import pytest

from flask import Flask, request, Blueprint, url_for
from json import dumps
import jwt
import hashlib
from data import *

class testLogin():
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.u_id = 0
    def emailTest(self):
        if email_check(self.email)=="Invalid Email":
            raise ValueError("Invalid Email Address")
    def passwordTest(self):
        if len(self.password) < 5:
            raise ValueError("Invalid Password Length")
    def login(self, email):
        if email != self.email:
                raise ValueError("Invalid Email Address")
    def pas(self, pas):
        if pas != self.pas:
            raise ValueError("Invalid Password")
    def valid(self):
        SECRET = 'COMP1531'
        return {'u_id': self.u_id, 'token': jwt.encode({'u_id':self.u_id}, SECRET, algorithm='HS256').decode('utf-8')}


#checking for bad email addresses
def test_auth_login1():
  
    test = testRegister("z5110036@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz")

    log = testLogin("z5110026@unsw.edu.au", "SomePassword")

    #this will not work as the email typed in isnt a valid email and 
    #doesnt match the one they used to sign up with
    with pytest.raises(ValueError, match='*Invalid Email Address*'):
        log.login("z5160026@unsw.au")
        
#checking for incorrect password
def test_auth_login2():

    #create a temp account
    test = testRegister("z5110036@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz")

    log = testLogin("z5110036@unsw.edu.au", "Someqwefhjb")
    
    #this wont work as an incorrect password is typed in
    #Trimesters != hello123
    with pytest.raises(ValueError, match='*Invalid Password*'):
        log.pas("Som")
            
#valid cases
def test_auth_login3():
    
    #create a temp account
    test = testRegister("z5110036@unsw.edu.au", "SomePassword", "Daniel", "Setkiewicz")
    log = testLogin("z5110036@unsw.edu.au", "SomePassword")
    
    #which should work, but with a proper token and not a dummy one
    SECRET = 'COMP1531'
    assert log.valid() == {'u_id': test.u_id, 'token': jwt.encode({'u_id':test.u_id}, SECRET, algorithm='HS256').decode('utf-8')}

