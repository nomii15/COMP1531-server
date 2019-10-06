##auth_login definition
import re
from email_check import *

'''
Given a registered users' email and password and generates a valid token for the user to remain authenticated

ValueError when:
Email entered is not a valid email
Email entered does not belong to a user
'''

def auth_login(email, password):
    
    if check_email(email) == "Invalid Email":
        raise ValueError("Invalid Email Address")
        
    #not a value password, example case 
    if password != "Hello123":
        raise ValueError("Incorrect Password")    
    
    #return token for frontend
    return "#"
    
