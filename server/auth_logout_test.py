import pytest
from auth_logout import *

#testing mix of correct and incorrent inputs
def test_auth_logout():
    assert(auth_logout("#") == "Deleted")
    assert(auth_logout("@") == "Not Deleted") 
    assert(auth_logout("whatisatoken") == "Not Deleted")
