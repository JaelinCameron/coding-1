# Discuss the anatomy of a function

# a function definition tells the computer 
# the instructions on what we want to do with data

# data = just means data types

# curly brackets = passing in data into
# the function definition. This is formally
# called a parameter

# parameter = placeholder for data

def modifyMyName(name):
    print('Your new modified name is the great '+ name)

# when we pass data into a function call it is called an
# arguement
# arguement = evidence, facts, real data.
# modifyMyName('Jaelin')





# Lesson on Conditional Statements

# conditional statements use the 'IF' and 'ELSE'
# keywords to filter and create specific outcomes 
# based on data

def vertifyAge(age):
    if age > 17:
        print('Congrats! You can buy GTA VI')
    elif age > 20:
        print('Sorry youre too old for this game.')
    else:
        print('Sorry, you need an adult to buy this game.')

#vertifyAge(19)

#Activity

def numberConversion(x):
    print('Your number has been converted into minutes')
    print(x)
    print(x * 60)

#numberConversion(3)  

# Conditional Statements 
# if /else keywords; gives us the ablity to
# control outcomes and make decisions on data 

# food expiration software is an example of 
#u using conditional statements. If the food expires 
# it needs to be thrown away, otherwise, or ekse 
# it can be eaten

def foodExpiration(month, date, year):
    expirationYear= 2024
    expirationMonth = 12
    expirationDate = 5
    if date > expirationDate and year > expirationYear: 
        print('throw food away.')
    else:
        print('The food is still good')

foodExpiration(12, 8, 2025)            
     