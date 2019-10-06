import pytest

def test_user_profile_setemail_correct():
    #setup part
    authRegDict = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token = authRegDic['token']
    Uid = authRegDic['u_id']
    #test part            
    user_profile_setemail(token,"Sad@gmail.com")
    UserPorfileDic = user_profile(token, Uid)
    assert(UserPorfileDic['email'] == "Sad@gmail.com"
    
def test_user_profile_setemail_invalid():
    #setup part
    authRegDict = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token = authRegDic['token']
    #test part         
    #invalid email address(assume Sad@abc is an invalid address)  
    with pytest.raises(ValueError, match=r"*"): 
        user_profile_setemail(token,"Sad@abc")
        
def test_user_profile_setemail_used():
    #setup part
    authRegDict1 = auth_register("Happy@gmail.com","qwe123","Happy","Man")
    token1 = authRegDic1['token']
    
    authRegDict2 = auth_register("Sad@gmail.com","123qwe","Sad","Woman")
    token2 = authRegDic2['token']
    
    #test part
    #email address is used
    with pytest.raises(ValueError, match=r"*"):            
        user_profile_setemail(token2,"Happy@gmail.com")


