#definition channels_listall function
from flask import Flask, request, Blueprint

# importing the data file
from data import *

'''
Provide a list of all channels (and their associated details)

'''

# maybe need to change route - double check later
@APP.route('channels/listall', methods['GET'])
def channels_listall():
    token = request.form.get('token')
    #add channel dictionary to add to global dictionary
    global data
    data = getData()

    return data['channels']