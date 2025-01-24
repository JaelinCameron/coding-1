numberList = [1,23,56,3,56,3,20,200]
numberList.reverse()
print(numberList)

def passwordLoops():
    correctPw= 'Homage'
    correct2Pw= '1.2'
    userPw = ''
    user2Pw = ''
    while userPw != correctPw:
        print('Incorrect pw. try agian')
        userPw = input('Please enter your password (Use only letters):')
        print('Congrats!')
        while user2Pw != correct2Pw:
            print('Incorrect pw. try agian')
            user2Pw = input('Please enter your password (Use only float):')
            print('Congrats!')
            
passwordLoops()
