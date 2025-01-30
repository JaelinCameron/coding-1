import random

# Loops - A construct in programing 
# where instructions will repeat over and
# over until a specific condition is met.

# While Loop - is a special type of loop where
#  instructions will repeat themselves
#  so long as a condition is true.

def repeatMs():
    x = 2
    while x == 2:
        print('This message will repeat forever. ') 

def passwordLoops():
    correctPw= '123abc'
    userPw = ''
    while userPw != correctPw:
        print('incorrect pw. try agian')
        userPw = input('please enter your password:')
    if userPw  == correctPw:
        print('Congrats!')
#passwordLoops()



def inventoryLoop():
    userInventory =[]
    pickUpItem= input('what item are you picking?')
    while len(userInventory) < 4:
      userInventory.append(pickUpItem)
      print('These are the items in your bag: ')
      print(userInventory)
      pickUpItem= input('what item are you picking?')

#inventoryLoop()

# save for another day def replaceInventoryItem():
# #def removeInventoryItem():

def rngGame(): 
    randomNumber = random.randrange(1, 11)
    print(randomNumber)
    userAnswer = ''
    while randomNumber != userAnswer:
        userInputGuess = int(input('Guess a number between 1 and 10:'))
        userAnswer = userInputGuess 
    if randomNumber != userAnswer:
        print('Incorrect Guess. Try agian')
    else:
        print('This is the correct answer')

# rngGame()

































# Create a function that uses a loop to check a password.
# if the password is correct,the loop will stop. If the password
# is incorrect the loop will continue.

# add in code that will provide a confirmation messehe to
# the iser, For example;  if the passwrod is correct , it should
# congradulate the user, and if its incorrect it
#  should tell them to try agian

def passwordSystem():
    correctPassword= 'stonegaurd73'
    userPassword = ''
    while userPassword != correctPassword:
        print('incorrect pw. try agian')
        userPw = input('please enter your password:')
    if userPassword  == correctPassword:
        print('Congrats!')
passwordSystem()





