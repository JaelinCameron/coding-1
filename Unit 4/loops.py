# What are loops
# Python loop is a programing concept where
# code repeats itself under specffic conditions.
 
# In Python, there are 2 version sof loops; for loop and
# while loop 

# While Loops- A type of loop that will repeat a
# set of instructions so long as some condition is true 


normAtk =2
SpecAtk =4
incrHp =3

def battleFunction():
    hp =10
    while hp >0:
        print('Do you want to attack?')
        print(hp) 
        hp -= normAtk
        keepGoing = input('do you want to keep playing')
        if keepGoing == 'y':
            print('Run function agian')
        else:
            print('Game over')

#battleFunction()
# For Loops - this is a type of loop that iterates over a collection
# of data and will run specific set of instructions on data.

# x in this a example is a iteraters. This x represents the numbers
# in the list

# For every number, we want to simply print it out   
numbers = [1,2,3,4,5,6,7,8]

#for x in numbers:
    #print(x)

attackValues =[10,25,50,90]

#for attacks in attackValues:
    #print('Level Up!')
   # print(attacks * 2)

# Create a function where items over $50.00 get a 10% dicount
def shoppingDiscountFunction():
    shoppingCart =['demo']
    cartCount = len(shoppingCart)
    print(cartCount)
    while len(shoppingCart) > 0:
        customerItem = input('How much does this item cost?')
        shoppingCart.append(shoppingCart)
        print('here are the item price in your cart: ')
        print(shoppingCart)

shoppingDiscountFunction()


