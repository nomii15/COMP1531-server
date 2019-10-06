import pytest

def test_user_profile_sethandle_correct():
    #setup part
    authRegDict = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token = authRegDic['token']
    Uid = authRegDic['u_id']
    #test part            
    user_profile_sethandle(token,"qwertyuiopasdfghjklzxcvbnm")
    UserPorfileDic = user_profile(token, Uid)
    assert(UserPorfileDic['handle_str'] == "qwertyuiopasdfghjklzxcvbnm"
    
def test_user_profile_sethandle_error():
    #setup part
    authRegDict = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token = authRegDic['token']
    #test part            
    with pytest.raises(ValueError, match=r"*"):
        user_profile_sethandle(token,"qwe")
