1. Other functions used in testing one function are all working correctly with no error raises. 
2. The first name and last name of the user should not be empty. 
3. The email address entered in user_profile function is valid. 
4. In the same test file, the information of user and channel are reset in each test function. 
5. The description of value error in user_profiles_uploadphoto function is wrong, the error should be exist when x_start, y_start, x_end, y_end are all out of the dimensions of the image at the URL and the dimensions are within 9999999999
6. After user registers his account for the first time using auth_register, he does not need to login using auth_login until he logouts using auth_logout. 
7. After user using channels_create to create a channel, he immediately becomes the owner of the channel. 
8. The email address and u_id for error testing are all invalid. 
9. In function channel_details, the return dictionary all_members includes the owners and it is ordered by the sequence of entrance. 
