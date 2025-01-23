def inventoryV2():
    userInventory =[]
    pickUpItem= input('what item are you picking?')
    if pickUpItem == 'sword':
       print('This is crucial to the game!')
    elif pickUpItem == 'food':
       print('Nice choice! You have a bag full of bread, meat, and fruit.')
    while len(userInventory) < 4:
      userInventory.append(pickUpItem)
      print('These are the items in your bag: ')
      print(userInventory)
      pickUpItem= input('what item are you picking?')

inventoryV2()

def questionGame():
    print('Welcome to the question game!')
    confirm= input('Press y to continue')
    if 'y':
      print('What continent is India in?')
    Answer=input('What is your answer?')
    elif 'Aisia':