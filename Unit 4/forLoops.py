
# FOR LOOPS - Is a type of loop that iterate over a list.
# it will go through your list and do whatever operation
# you want it to do.
  
# for loops use an iterator, which is just a varible
# that is intended to represent a value in the list.

# the "IN" keyword gives us access to the list we
# want to go through

def grocery():
    groceryList =['apple','water','milk','chicken']
    for x in groceryList:
        if x == 'milk':
            continue
        print(x)

gradeList =[100, 70, 90, 70, 65, 95]

def gradeRemove():
    for grade in gradeList:
        if grade < 75:
                continue
        print(grade)

for grade in gradeList:
     gradeList.append(85)
     print(grade)
     break

# add all the number together and then return the
# value in the for loop 