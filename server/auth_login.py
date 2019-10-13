##auth_login definition
import re
from email_check import email_check
# import the function and the global dictionary
import auth_register

'''
Given a registered users' email and password and generates a valid token for the user to remain authenticated

ValueError when:
Email entered is not a valid email
Email entered does not belong to a user
'''

global auth_register.data{}

def auth_login(email, password):
    
    if check_email(email) == "Invalid Email":
        raise ValueError("Invalid Email Address")
        
    #not a value password, example case 
    #if password != "Hello123":
    #    raise ValueError("Incorrect Password")   

    # find the user
    for user in global auth_register.data{}:
        if user['email'] == email:
            if user['password'] == password:
                # login and break
                ret{}
                ret['u_id'] = user['name_first'] + user['name_last']
                ret['token'] = "#" #temp token
                return ret
            else:
                # password doent match
                # throw error
        else:
            pass

    # if get to here, email isnt associated with an account
    # return error, email not associated with a account
    
    
    
