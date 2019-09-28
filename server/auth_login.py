##auth_login definition
import re

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
    
    
    
    
##this could be in its own file and import to projects when needed.
    
#logic for check email function comes from
#https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/    
def check_email(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        return "Valid Email"
    else:        
        return "Invalid Email"

