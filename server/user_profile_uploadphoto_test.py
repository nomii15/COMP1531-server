import pytest

def test_user_profile_uploadphoto_correct():
    #setup part
    authRegDict = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token = authRegDic['token']
    
    #test part
    #assume x_start, y_start, x_end, y_end are all within the dimensions
    user_profiles_uploadphoto(token, 200, 100, 100, 100, 100)
    
    
    
def test_user_profile_uploadphoto_error1():
    #setup part
    authRegDict = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token = authRegDic['token']

    #test part
    #img_url is return an HTTP status other than 200
    with pytest.raises(ValueError, match=r"*"):
        user_profiles_uploadphoto(token, 300, 100, 100, 100, 100)
        
def test_user_profile_uploadphoto_error2():
    #setup part
    authRegDict = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token = authRegDic['token']

    #test part
    #x_start, y_start, x_end, y_end are out of the dimensions
    with pytest.raises(ValueError, match=r"*"):
        user_profiles_uploadphoto(token, 200, 9999999999, 9999999999, 9999999999, 9999999999)
