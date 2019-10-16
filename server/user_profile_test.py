import pytest
def test_user_profile_correct():
    #setup part
    authRegDict = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token = authRegDic['token']
    Uid = authRegDic['u_id']
    #test part
    UserProfileDic = user_profile(token, Uid)
    assert(UserProfileDic['email']) == "Happy@gmail.com"
    assert(UserProfileDic['name_first']) == "Happy"
    assert(UserProfileDic['name_last']) == "Man"
    assert(UserProfileDic['handle_str']) == "HappyMan"
    
def test_user_profile_invalid():
    #setup part
    authRegDict = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token = authRegDic['token']
    Uid = authRegDic['u_id']
    #ensure Uid2 will not coincide with Uid
    Uid2 = Uid + 1
    #test part
    with pytest.raises(ValueError,match=r"*"):
        UserProfileDic = user_profile(token, Uid2)
        


