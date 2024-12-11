# Functions are just instructions
# for the computer to know what to do
# with data.

# conditional statemenents use the if/ else 
# keywords to make decisions and outcomes
# based on data.

def welcomeMsgByTime(number, time):
    if time == 'am':
        print('Good Morning.')
        print(str(number) + time)
    elif time == 'pm':
        ('Good Evening ')
        print(str(number) + time)
    else:
        print('Sorry, did not understand your input, please try agian')

#welcomeMsgByTime(8,'pm')







def gradingSystem(percentage):
    if percentage >= 90:
        print('Congratulations! You have an A.')
    elif percentage >= 80:
        print('Congratulations! You have an B.')
    elif percentage >= 70:
        print('Congratulations! You have an C.')
    elif percentage > 100:
        print('Sorry you need to put a grade in the 100-0 range')
    elif percentage < 0:
        print('Sorry you need to put a grade in the 100-0 range')    
    else:
        print('Sorry, but you are failing try to get your grade higher.')

gradingSystem()

