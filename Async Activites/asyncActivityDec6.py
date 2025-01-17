# Create a function that will accept a word in the function parameter 
# and return the word in reverse order. For example, the word 'pet' should 
# return as 'tep', the word 'book' should return as 'koob', etc. HINT-
# There is a built-in function that you can use to accomplish this. 
# Please use W3 schools to research what function you'll need to use.

def my_function(word):
     txt = word[::-1]
     print(txt)


my_function("food")   
my_function("pet")
my_function("book")

# Create a function that uses a conditional statement to
# output a block of text that will tell users about a states landmarks.
# Your program should return the following states and their respective landmarks.
# For example, if a user passes in the value of south carolina, in the function parameter,
# your program should return the message: ' 
# A landmark in South Carolina is Fort Sumter, where the inital shots of the
# ' 'American Civil war took place.' WRITE A COMPLETE SENTENCE!

def landmark_info(State):
  if State == "Pennsylvania":
    print("A landmark in Pennsylvania is Liberty Bell, previously called the State House Bell or Old State House Bell, is an iconic symbol of American independence")
  elif State == "New_York":
    print("A landmark in New york is The Statue of Liberty, a National Monument is a United States national monument comprising Liberty Island and Ellis Island")
  elif State == "California":
    print("A land mark in California is the Hollywood Walk of Fame, a landmark which consists of 2,800 five-pointed terrazzo-and-brass stars embedded in the sidewalks along 15 blocks of Hollywood Boulevard and three blocks of Vine Street in the Hollywood district of Los Angeles.")
  elif State == "Puerto_Rico":
    print("A land mark in Puerto Rico is El Morro, a large fortress and citadel in the historic district of Old San Juan in Puerto Rico")
  else:
    print("Sorry this State is not registered")

landmark_info("California")   

  