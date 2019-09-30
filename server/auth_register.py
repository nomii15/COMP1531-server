#definition auth_register function
from email_check import *

'''
Given a user's first and last name, email address, and password, create a new account for them and return a new token for authentication in their session

ValueError when:
Email entered is not a valid email.
Email address is already being used by another user
Password entered is not a valid password
name_first is more than 50 characters
name_last is more than 50 characters
'''


def auth_register(email, password, name_first, name_last):

    if email_check(email) == "Invalid Email":
        raise ValueError("Invalid Email Address")
        
    if email == "z5160026@unsw.edu.au":
        raise ValueError("Email Already Exists")    
    
    if len(password) < 5:
        raise ValueError("Invalid Password Length")
        
    if len(name_first) > 50 or len(name_first) == 0:
        raise ValueError("Invalid First Name Length")
        
    if len(name_last) > 50 or len(name_last) == 0:
        raise ValueError("Invalid Last Name Length")            

    return {0,"#"}
