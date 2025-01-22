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

inventoryLoop()