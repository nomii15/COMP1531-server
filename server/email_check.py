#definition for check email function comes from
#https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/    

import re

def email_check(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        return "Valid Email"
    else:        
        return "Invalid Email"

