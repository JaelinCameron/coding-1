import random
# ROCK, PAPER, SCISSOR GAME APP
# You are working on a game concept with several 
# other engineers and you need to provide them with a
#  simple proof of concepts. 
# For now, you have suggested that your 
# game work on a RPS (rock, paper, scissors) loop. 
# When a user plays, rock, paper, or scissors, 
# the computer will randomly select one of the 3 
# options as well. Your program will then determine 
# who won, based on the values. The game should only 
# allow the player to play 3 hands, and inform the 
# player if the won or lost (best 2 out of 3 format.) 

#  1. What is the problem asking you to do?
# The problem is asking me to make a program that randomly chooses between RPC that 
# also outputs if the player wins

# 2. What are some keywords and phrases ? 
# Randomly selects
# 3 hands


# 3. Is there input data that the question provides ?
# We need to be able to put in either RPC


# 4. What is the desired output ?
# If the player wins or lose 


# 5. Pseudocode Steps & Additional Notes 
# import Random 
# random.choice
# while loop
# if else conditionals 

# Solution

def rpc():
    mylist = ["rock", "paper", "scissors"]
    print(random.choice(mylist))
    playerchoice= int()
    gamepoint=0
    while gamepoint <= 3:
        if playerchoice == "paper" and mylist == "rock":
            gamepoint= 