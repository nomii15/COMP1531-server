import pytest
def test_user_profile_setname_correct():
    #setup part
    authRegDict = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token = authRegDic['token']
    Uid = authRegDic['u_id']
    #test part          
    user_profile_setname(token,"Sad","Boy")
    UserPorfileDic = user_profile(token, Uid)
    assert(UserPorfileDic['name_first'] == "Sad"
    assert(UserProfileDic['name_last'] == "Boy"
    
def test_user_profile_setname_error_firstname():
    #setup part
    authRegDict = auth_register("Happyy@gmail.com","qwe123","Happyy","Woman")
    token = authRegDic['token']
    Uid = authRegDic['u_id']
    
    #test part
    with pytest.raises(ValueError, match=r"*"):
        user_profile_setname(token,"qwertyuiopasfghjklzxcbnmqwetuiopqwetuiopqwetuiopqwetuiopqwetuiop","Girl")
        
def test_user_profile_setname_error_lastname():
    #setup part
    authRegDict = auth_register("Happyyy@gmail.com","qwe123","Happyyy","Boy")
    token = authRegDic['token']
    Uid = authRegDic['u_id']
    #test part
    with pytest.raises(ValueError, match=r"*"):
        user_profile_setname(token,"Sad","qwertyuiopasfghjklzxcbnmqwetuiopqwetuiopqwetuiopqwetuiopqwetuiop")
        

