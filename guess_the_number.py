#importing randrange to choose a number by a comp. randomly
from random import randrange
#import math for initializing inf for user_guess variable
import math 

lower_bound =int(input("please enter the lower bound: "))
higher_bound = int(input("please enter the higher bound: "))

def guess_the_number_user(lower_bound, higher_bound):
    number_to_guess = randrange(lower_bound, higher_bound)

    #inf_to make it difficult for a user tu guess the number at once
    user_guess = math.inf
    trials_amount = 0    

    while number_to_guess != user_guess:
        trials_amount=trials_amount+1
        user_guess = int(input(f"Guess the number between {lower_bound} and {higher_bound}: "))
        if user_guess<number_to_guess:
            print ("the number is small, try higher: ")
        elif user_guess>number_to_guess:
            print ("the number is high, try smaller: ")
      

    print(f"You win {number_to_guess} in {trials_amount} trials")
guess_the_number_user(lower_bound, higher_bound)
   
