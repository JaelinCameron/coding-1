# Data types- level 1: must bsic building block of 
# code, (number, letters, true or false)

# operators- level 2: the ablitity to manipulate and 
# do things with data types 
# (math, comparisons, assignment, etc...)

# function- level 3: taking the first two concepts and 
# organizing these operations and data types 
# into instructions 

# conditional statement: level 3a: being able 
# to add more control  on our function instructions



# Billing System Function
# Goal: To he able to check and see if a user is past
# due or up-to-data on their subscriptions

# user - username string
# user - userPaymentDate = string/ integer
# user - PaymentAmount = integer


# we need to know if their account is 
# past due OR up-to-date

# function definition- tells the computr what the
#  function actually does and how its supposed to work
def checkSubscriptions(userDueDate, userMoneyInAccount):
   if userDueDate == 6:
        if userMoneyInAccount == True:
            print('subscriptionis paid - auto withdraw payment.')
        else:
            print('payment still do- could not withdraw funds.')  
    else:
       print('Your ')

checkSubscriptions(6, False)