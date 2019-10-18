#implementation of search function
from json import dumps
from flask import Flask,request
import jwt

APP = Flask(__name__)


@APP.route('/search', methods=['GET'])
def search():
    messages = {}

    token = request.args.get('token')
    query_str = request.args.get('query_str')

    # get the dictionary to compare members of channel with user

    # compare channels which the user is in

        # look through the messages and compare with the query str

        # if match, add to a dictionary


    #return the dictionary of items associated with query string 
    return dumps(messages)  

