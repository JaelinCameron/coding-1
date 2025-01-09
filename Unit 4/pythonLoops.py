# Create a function that will determine what level of education
# level of education a collage student is in 
# based on the number of years they've been in 
# school.

# undergrad 1 freshman, 2 sophmore, etc....
# 5> masters degree, doctorate degree, etc....

collegeTitles= ['You dont have a college title (yet)','Freshman','Sophmore','Junior','Senior']
print(len(collegeTitles))
# collegeTitles.length()

def titleBySchoolYear():
    # input is a built-in function that lets us pass data into our 
    # program AS STRINGS

    # int() is also is a built in function that transform anything inside
    # of its round brakets into a interger number.
    # the first 3 letters of interger are INT
    #   
    year = int(input('how many years of college do you have? '))
    if year == '0':
        print(collegeTitles[0])
    if year == '1':
        print(collegeTitles[1])
    elif year == '2':
        print(collegeTitles[2])     
    elif year == '3':
        print(collegeTitles[3])
    elif year == '4':    
        print(collegeTitles[4])
    elif year >= 7 and year <= 10:
        print('You are in a doctorates program and in grad school.')
    elif year >11:
        print('Excuse me, you need to find a job. You have been in school to long.')    
    else:
        print('Error: something went wrong. please check your input.')

titleBySchoolYear()

# A list is a data type for collecting and organizing other data types.

# We create a list by giving it a varible name and
# using the square brakets to place the data inside of it

list8 =[10,102,4904]

listOfData = ['words and characters',
             10,
             10.2324,
             True,
             False,
             list8
             ]
#print(listOfData)

collegeTitles= ['You dont have a college title (yet)','Freshman','Sophmore','Junior','Senior']

#print(collegeTitles[0])