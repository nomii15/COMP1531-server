#definition auth_register function
from email_check import email_check
from flask import Flask, request
from json import dumps
import jwt
import hashlib

APP = Flask(__name__)

SECRET = 'COMP1531'

# global variable for users

user = 0
data = {
    'users': {} 
}

def getData():
    global data
    return data

def getSecret():
    global SECRET
    return SECRET    

def getUsers():
    global user
    return user

def incUser():
    global user
    user+=1        


@APP.route('/auth/register', methods=['POST'])
def auth_register():

    email = request.form.get('email')
    password = request.form.get('password')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')

    #check if valid email
    if email_check(email) == "Invalid Email":
        raise ValueError("Invalid Email Address")
    
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
    data = getData()
    user = getUsers()
    data['users'][user] = {'email': email, 'password': hashlib.sha256(password.encode()), 'name_first': name_first,
     'name_last': name_last}
    incUser()

    #think about implementing a variable for u_id within data
    #currently, two names may clash

    # return a dictionary of u_id and token
    ret = {}
    u_id = name_first.lower() + name_last.lower()
    u_id = ''.join(u_id)

    # if the u_id is greater than 20 character, reduce
    if len(u_id)>20:
        u_id = u_id[0:19]

    SECRET = getSecret()

    ret['u_id'] = u_id
    ret['token'] = jwt.encode({'u_id': ret['u_id']}, SECRET, algorithm='HS256').decode('utf-8')

    return dumps(ret)

@APP.route('/auth/login', methods=['POST'])
def auth_login():

    email = request.form.get('email')    
    password = request.form.get('password')

    if email_check(email) == "Invalid Email":
        raise ValueError("Invalid Email Address")
        

    # find the user
    #data = getData()
    #print(data['users'])
    i = 0
    data = getData()
   # print("============")
   # print(data)
   # print("============")
    for em, pas in data['users'].items():
        #print(em)
        #print(pas)
        if pas['email'] == email:
            if pas['password'].hexdigest() == hashlib.sha256(password.encode()).hexdigest():
                # login and break
                ret = {}
                u_id = pas['name_first'].lower() + pas['name_last'].lower()
                u_id = ''.join(u_id)
                ret['u_id'] = u_id
                # if the u_id is greater than 20 character, reduce
                if len(u_id)>20:
                    u_id = u_id[0:19]
                ret['token'] = jwt.encode({'u_id': ret['u_id']}, SECRET, algorithm='HS256').decode('utf-8')
                return dumps(ret)
            else:
                raise ValueError("Invalid Password")
        else:
            pass
        i+=1    

    raise ValueError("Incorrect Email address")
    # if get to here, email isnt associated with an account
    # return error, email not associated with a account

if __name__ == '__main__':
    APP.run(port=20000, debug=True)
