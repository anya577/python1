#importing randrange to choose a number by a comp. randomly
from random import randrange
#import math for initializing inf for user_guess variable
import math 
import string

#enables a user to choose between the modes: human-guess option or computer-guess option
def main():
    
    game_mode = int(input("Choose game mode \n User guess the number, press 1\n Computer guess the number, press 2 \n  " ))

# 1-human-guess mode    
    lower_bound =int(input("please enter the lower bound: "))
    higher_bound = int(input("please enter the higher bound: "))
   

    if game_mode == 1:
        guess_the_number_user(lower_bound, higher_bound)
    elif game_mode == 2:
            guess_the_number_computer(lower_bound, higher_bound)
   
# game-mode wrong symbol:
    
    # mode_mistake = string(input('choose only from 1 or 2 '))    
    # if mode_mistake !=1 or mode_mistake !=2:
    #     print('choose only from 1 or 2 ')

    
    main()
    return 0
         
  


def guess_the_number_user(lower_bound, higher_bound):
    number_to_guess = randrange(lower_bound, higher_bound)

# infinity assignment 
    user_guess = math.inf
    trials_amount = 0 
          
    while number_to_guess != user_guess:
        trials_amount=trials_amount+1
        user_guess = int(input(f"Guess the number between {lower_bound} and {higher_bound}: "))
        
        if user_guess<number_to_guess:
            print ("the number is small, try higher: ")
        elif user_guess>number_to_guess:
            print ("the number is high, try smaller: ")    
        elif user_guess<lower_bound:
            print ('number must be between lower and higher numbers')     

    print(f"Congratulations! You win {number_to_guess} in {trials_amount} trials")

    
# calculating score
    game_over = input('to return to main meny, press the (m) button. \n To quit the game, press ENTER ')
    if game_over=='m':
        print('------------------------------------------------------ \n')
        main()

        return 0    

        
        
#2- mode: number is guessed by a comp   

def guess_the_number_computer(lower_bound, higher_bound):
    feedback = ' '
    computer_guess = math.inf
    guess_counter=0        
    while feedback != 'c':
        guess_counter +=1    
        computer_guess = randrange(lower_bound, higher_bound)
        feedback = input(f"is {computer_guess} correct (c), too low (l), too high (h):  ")
        if feedback == 'l':
            lower_bound = computer_guess+1
        elif feedback == 'h':
            higher_bound = computer_guess-1 
        if lower_bound==higher_bound:
            guess_counter+=1
            print (f'congratulation! it is {lower_bound}')
            computer_guess=lower_bound
            break   
               
    print (f'computer guessed the number {computer_guess} in {guess_counter} trials') 
      
    

    #end of the game with options: quit or start again  
    game_over = input('to return to main meny, press the (m) button. To quit the game, press ENTER ')
    if game_over=='m':
        print('------------------------------------------------------\n')
        main()
    return 0

main()    
                  

