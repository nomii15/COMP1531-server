Assumptions

1)  The variables first_name and last_name cannot be empty (i.e. “”). This is to assure that u_id is not blank.

2)  When testing individual functions, if that function being tested depends on another; it is assumed that function is working correctly.

3)  When creating test scenarios of functions for iteration 1, the exact data structure which the information is stored is assumed and could change when implementing the actual function.

4)  When using the search function, an error is thrown when the user is looking for a message which is greater than 1000 characters.

5)  The search function also looks for the prefix of a query string. 

6)  The email address entered in user_profile function is valid. 

7)  In the same test file, the information of user and channel are reset in each test function.

8)  The description of value error in user_profiles_uploadphoto function is wrong, the error should be exist when x_start, y_start, x_end, y_end are all out of the dimensions of the image at the URL and the dimensions are within 9999999999

9)  After user registers his account for the first time using auth_register, he does not need to login using auth_login until he logouts using auth_logout. 

10) After user using channels_create to create a channel, he immediately becomes the owner of the channel. 

11) The email address and u_id for error testing are all invalid.

12) In function channel_details, the return dictionary all_members includes the owners and it is ordered by the sequence of entrance.
