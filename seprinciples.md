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

6. As a team, we also decided to seperate our functions as much as possible, where each function which was responsilble for a certain task in the overall software was maintained in a separate file. This was done as we felt it made it clearer and easier to understand where everything was and what purpose it served. This demonstrated the modularity SE Principle, and to an extent, the princple of Anticpation of Change, as factoring our code in such a way, made it significantly easier to modify our functions if and when the time came.

7. Due to the nature of the project and the continuous flow of changing requirements form Sally and Bob as well as our care in not implementing too many functionalities in one go, we felt that we excerised Incrmental Developement to a sound standard. For example, in scenarios such as our data structure, we initially formed a template of how we thought it should be structured, and slowly we would add different nodes and keys like the storage of the images, which was to make sure our developement process was a seemless as possible. 

8. In literation 3, we implement software engineering principle to make our code simpler. For testing functions in literation 1 and 2, we created one token for every registered user in user_test functions and one extra channel for the purpose of testing exceptions in channel_test functions. In this iteration, we delete the unused token and try to use the same channel for different exception testing to simplify our code.

9. Our functions for checking invalid input only has single responsibility for one exception. For file channel_check, it used to have only one function in it which is responsible for checking invalid channel_id and members. It only returns True when both of the inputs are valid. We separate the function into member_check and channel_check to ensure each function is only responsible for one exception.

