# In your own words, describe what a function is. Please write your response in a complete sentence as a string data type.
# A function is is a set of instruction that preform a specific task or job.

# In your own words, describe the difference between a function parameter and a function argument. Please write your response in a complete sentenc as a string data type.
# A function parameter is a placeholder for data, while an function argument is when you pass in data for the function.

# In your own words, describe what an if/ else conditional statement is. Please write your response in a complete sentence as a string data type.
# The if/ else conditional statements are keywords to make decisions or outcomes based on data in the function arguement.

# What is an integer data type? Please write your response in a complete sentence as a string data type.
# The integer data type is data that is all whole numbers.

# What is a boolean data type? Please write your response in a complete sentence as a string data type.
# The boolean data type is something to check data to see if it is true or false.

# Which operator would work best for the following function
# An age verification function that needs to check if a user is a certain age and older to purchase a video game. Please write your answer as a string.
# The operator that would work best for the following function would be the comparison operator.

# Which operator would work best for the following function:
# An office security function that needs to have a specific alpha-numeric code to be entered in order to enter and exit a building. Please write your answer as a string.
# The operator that would work best for the following function would be the assignment operator.

# You have been hired by Github to help them fix their password system. They would like you to create A function that will check how long a password is.
#  Your program should be able to accept a alpha-numeric password and check if the password is more or less than 10 characters long. 
# if the password is longer than 10 characters, your program should tell the user that their password is too long. 
# If the password is under 4 characters the function should tell the user the password is too short. 
# If the password meets the length criteria, there should be a message confirming to the user that their password was created successfully.

def alphaNumricPasswordSystem(password):
    txt= password
    password = txt.count(password, 4, 10)
    if password.count < 4:
        print('This password is too short please enter another one.')

alphaNumricPasswordSystem(1)