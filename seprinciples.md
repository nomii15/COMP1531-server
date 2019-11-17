Through the transition from iteration 2 to iteration 3, we felt the need to incorporate some SE design principles in our code. Some of the changes we made throughout our functions are,

1. Across most of our functions, there were a few repetitve processes that we realised we were all writing up. For example tasks such as retreiving the user_id from the token or checking if a user was a channel owner, were tasks which we felt could be dealt with more efficiently. Therefore, to improve consistency across our functions in terms of how we perform these tasks as well as to reduce code repetition, we decided to create helper functions that we could all import and call from within our own functions. These were, 

        -token_check
    
        -member_check
    
        -token_to_uid
    
        -check_channel_owner
    
    Doing this, allowed us to meet the DRY criteria of not having the same piece of code written multiple times across multiple functions. 

2. When completing some of the message functions, specifically message_edit, the time complexity of checking the owner of the message and editing the message was extremely high (sometimes O(n^4 )). This obviously bore some design smells such as opacity and needless complexity as some of these functions were difficult to read and understand. After refactoring the code, the message functions were greatly improved in terms of their complexity with most staying at a maximum of O(n^2 ).

3. A major problem we encountered when attempting to run the server with the frontend was that the message id's we were assigning to each message sent was unique only to the channel the message was sent to and not to the complete application in a global sense. This proved to be an issue because there resulted messages in different channels having the same message id's. The problem occured when the frontend would request a message_id because obviously there were multiple messages with that id. When attempting to modify our code, we found it difficult because of the immobility and rigidity of our original code. As a result of this, the message structure was reworked, where we decided to make the message_id unique to the message in a global environment. This also helped reduce the coupling between the message id and the channel that message was asociated in.

4. Common across a lot of the functions was the readability of the code. in most cases, although the logic seemed to work, it was very difficult to intrepret and gain an understanding what was actually going on. To solve this, functions were rewritten to make it clearer what exactly was happening throughout the logic. An example of this was in the admin userpermision change function, where a rethink of the structure and logic was needed to better intrepret what was happening within that function.

5. When it comes to testing of our functions, this needed to be changed from iteration2 due to complexity of how our group was calling the flask requests within the route of the function. This made it incredibly difficult to properly test our functions as we had to make a lot of assumptions about our test environment. For this iteration, we improved this by removing the flask requests into a flask specific function and the main function was called with the parameters it requires. This change makes it alot more efficient to properly test our code and make sure we are covering all edge cases. 






