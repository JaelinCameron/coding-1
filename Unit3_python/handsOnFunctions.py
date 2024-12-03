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

vertifyAge(19)