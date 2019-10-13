#definition auth_register function
from email_check import email_check

'''
Given a user's first and last name, email address, and password, create a new account for them and return a new token for authentication in their session

ValueError when:
Email entered is not a valid email.
Email address is already being used by another user
Password entered is not a valid password
name_first is more than 50 characters
name_last is more than 50 characters
'''

# global variable
global data
data = {}

def auth_register(email, password, name_first, name_last):

   #check if valid email
    if email_check(email) == "Invalid Email":
        raise ValueError("Invalid Email Address")
    
   #dummy case to check email already has a account created    
   #if email == "z5160026@unsw.edu.au":
   #   raise ValueError("Email Already Exists") 
   #
   # need to inplement this when perm data structure is decided   
    
   #password length check
    if len(password) < 5:
        raise ValueError("Invalid Password Length")
        
   #first name length check    
    if len(name_first) > 50 or len(name_first) == 0:
        raise ValueError("Invalid First Name Length")
    
   #last name length check   
    if len(name_last) > 50 or len(name_last) == 0:
        raise ValueError("Invalid Last Name Length")


   # add user dictionary to add to the global dictionary

   # create new user to the data dictionary, need to check syntax
    data[len(data)] = {}
    data[len(data)]['name_first'] = name_first
    data[len(data)]['name_last'] = name_last
    data[len(data)]['password'] = password
    data[len(data)]['email'] = email

    #think about implementing a variable for u_id within data
    #currently, two names may clash

    # return a dictionary of u_id and token
    ret = {}

    ret['u_id'] = name_first + name_last
    ret['token'] = "#" # temporary return token

    return ret
