def intergerDection(x):
    if x > 0:
        print("This number is positive")
    elif x == 0:
        print("This number is zero")
    else:
        print("This number is negitve")
       

intergerDection(2)
intergerDection(0)
intergerDection(-2)


def netflixAge(Age):
    if Age <= 10 or Age >= 65:
        print("You have to pay $5.00")
    elif Age <= 16 or Age >= 16: 
        print("You have to pay $10.00")
    elif Age >= 20:
        print("You have to pay $15.00")

netflixAge(20)