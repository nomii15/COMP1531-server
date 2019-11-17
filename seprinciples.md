Throughout the course of writting functions from iteration2 to iteration3, some of 
the refracturing changes that our group encorporated into the functions
design are, 

1. Across a lot of the functions, similar processes were being done; e.g. getting a
uid from a token. With this, helper functions were created to inprove consistency
and to make sure our group was doing the same process to extract something. Examples 
of this include token_check, member_check, token_to_uid. As a result, this reduce the code
repetition by only having one written instance of it and meets the DRY criteria of
not having the same piece of code writtem mulitple times accross multiple functions

2. When writting some of the message functions, the orginial time complexity of 
the function were very high (order 3 or 4 in most cases). As a result, this
made the function difficult to understand (Opacity) and also adding a hiigh level of 
needless complexity. After the refractoring of the code, most of the functions are
around order 1 or 2, making it more time efficient when searching for an item. Particular
functions were this was most evident was message reacts/unreacts and pin/unpin.

3. One of the problems which we initially had with the message id was that they 
were originally related to the channel and not unique globally. i.e. each channel 
would of had a message_id that was the same in another channel. this created problems
when the frontend would request a message id that would appear in multiple channels.
when attempting to modify our original code, the code was difficult to modify to 
work with the modifications needed (immobility and rigidity). As a result of this, the message
structure was rewritten and made such that the message id is unique to each message
globally. This also helped reduce the coupling between the message id and the
channel that message was asociated in.

4. Common across a lot of the functions was the readability of the code. in most cases,
although the logic seemed to work, it was very difficult to intrepret and gain an understanding
what was actually going on. To solve this, functions were rewritten to make it
clearer what exactly was happening throughout the logic. An example of this was
in the admin userpermision change function, were a rethink of the structure and 
logic was needed to better intrepret what was happening within that function.

5. When it comes to testing of our functions, this needed to be changed from
iteration2 due to complexity of how our group was calling the flask requests within
the route of the function. This made it incredibly difficult to properly test our
functions as we had to make a lot of assumption about our test environment. For this 
iteration, this has been improved this by removing the flask requests into a flask specific function
and the main function was called with the parameters it requires. This change makes
it alot more efficient to properly test our code and make sure we are covering 
all edge cases. 






