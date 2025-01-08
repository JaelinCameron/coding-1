# Create a function that will determine what level of education
# level of education a collage student is in 
# based on the number of years they've been in 
# school.

# undergrad 1 freshman, 2 sophmore, etc....
# 5> masters degree, doctorate degree, etc....

def gradeToTitle():
    year = int(input('What year are you in?'))
    if year == 1:
        print('You are a Freshman in undergrad.')
    elif year == 2:
        print('You are a Sophmore in undergrad.')     
    elif year == 3:
        print('You are a Junior in undergrad.')
    elif year == 4:    
        print('You are a Senior in undergrad')
    elif year == 5 or year == 6:
        print('You are in masters program and in grad school.')  
    elif year >= 7 and year <= 10:
        print('You are in a doctorates program and in grad school.')
    elif year >11:
        print('Excuse me, you need to find a job. You have been in school to long.')    
    else:
        print('Error: something went wrong. please check your input.')

gradeToTitle()