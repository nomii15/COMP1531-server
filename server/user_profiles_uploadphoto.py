from data import *
import jwt
from flask import Flask, request, Blueprint, send_from_directory
from json import dumps
import urllib.request
import sys
from PIL import Image
import imghdr
from token_to_uid import token_to_uid
from token_check import token_check

def users_profiles_uploadphoto(token, img_url, x_start, x_end, y_start, y_end):
    
    #error handling for inputs
    if token_check(token) == False:
        raise ValueError(descripton = "Invalid token")    

    #error for image not being a jpeg image
    # retrieve u_id from token
    u_id = token_to_uid(token)
    port = sys.argv[1]
    url = f"http://127.0.0.1:{port}/static/"
    name = f"./static/{u_id}.jpeg"
    try:
        urllib.request.urlretrieve(img_url, name)
    except Exception as e:
        if type(e) != 200:
            raise ValueError(description = "HTTP status not 200")
        elif imghdr.what(name) != 'jpeg':
            raise ValueError(description = "Image not a jpeg image")
        else:
            pass


    # add checks to see if that values are correct inputs

    #crop the url image
    imageobject = Image.open(name)

    #check the dimensions of the image
    width, height = imageobject.size
    print(width)
    print(height)
    if x_end - x_start > width:
        raise ValueError(description = "invalid x coordinates")
    if y_end - y_start > height:
        raise ValueError(description = "invalid y coordinates")    


    cropped = imageobject.crop( (x_start,y_start,x_end,y_end) )
    cropped.save(name)

    #print("get here")

    #save img url in users details
    for i, items in data['users'].items():
        if items['u_id'] == u_id:
            items['profile_img_url'] = url + f"{u_id}.jpeg"
            #print(items['profile_img_url'])
            break

    #send to server
         
    
    return





uploadphoto = Blueprint('uploadphoto', __name__)
@uploadphoto.route('/user/profiles/uploadphoto', methods=['POST'])
def upload():

    token = request.form.get('token')
    img_url = str(request.form.get('img_url'))
    x_start = int(request.form.get('x_start'))
    x_end = int(request.form.get('x_end'))
    y_start = int(request.form.get('y_start'))
    y_end = int(request.form.get('y_end'))
    users_profiles_uploadphoto(token, img_url, x_start, x_end, y_start, y_end)
    return dumps( {} )
