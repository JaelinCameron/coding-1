campingSupplies = ['tent','sleeping bag','flash light','camping knife']
campingSupplies.reverse()
print(campingSupplies)

def campingAddtion(item):
        campingSupplies = ['tent','sleeping bag','flash light','camping knife']
        if item == 'medkit':
            campingSupplies.append('medkit')
            print(campingSupplies)

campingAddtion('medkit')

food = ["apple", "pizza" , "blueberry"]
seasoning = ['salt', 'pepper', 'paprika']

food.extend(seasoning)
print(food)

campingItems = ['tent','sleeping bag','flash light','camping knife']
campingItems[2] = 'camp fire kit'
print(campingItems)

