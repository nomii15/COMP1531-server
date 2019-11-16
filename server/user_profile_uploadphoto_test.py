import pytest
from auth_register import auth_register
from user_profiles_uploadphoto import users_profiles_uploadphoto
from data import *

'''
def test_user_profile_uploadphoto_correct():
    #setup part
    authRegDic = auth_register("Hapcpy@gmail.com","qwe123","Happy","Man")
    token = authRegDic['token']
    url = "http://www.news.tracanada.ca/wp-content/uploads/2017/07/curata__fhH3JcHUGmZPaVe.jpeg"
    #test part
    #assume x_start, y_start, x_end, y_end are all within the dimensions
    users_profiles_uploadphoto(token, url, 0,0,100,100)
    assert( data['users'][1]['img_profile_url'] != None )
'''
    
def test_user_profile_uploadphoto_error1():
    #setup part
    authRegDic = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token = authRegDic['token']
    url = 'http://www.news.tracanada.ca/wp-content/uploads/2017/07/curata__fhH3JcHUGmZPaVe.jpeg'

    #test part
    #img_url is return an HTTP status other than 200
    with pytest.raises(ValueError, match=r"*"):
        users_profiles_uploadphoto(token, "somefakeimage.png", 300, 100, 100, 100)
        
def test_user_profile_uploadphoto_error2():
    #setup part
    #authRegDict = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    #token = authRegDic['token']
    url = "http://www.news.tracanada.ca/wp-content/uploads/2017/07/curata__fhH3JcHUGmZPaVe.jpeg"
    authRegDic = auth_register("Hfappy@gmail.com","qwe123","Happy","Man")
    token = authRegDic['token']

    #test part
    #x_start, y_start, x_end, y_end are out of the dimensions
    with pytest.raises(ValueError, match=r"*"):
        users_profiles_uploadphoto(token, url, 9999999999, 9999999999, 9999999999, 9999999999)
