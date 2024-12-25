# import random

# target_number = random.randint(0,100) # generating a random number
# guesses = 0
# low = 0
# high = 100
# while True:
#     print(f"Range: {low} --> {high}. Your guess?", end = " ")
#     guess = int(input())
#     guesses += 1

#     if guess < target_number:
#         print("Incorrect!")
#         low = guess + 1
#     elif guess > target_number:
#         print("Incorrect!")
#         high = guess - 1
#     else:
#         print("Congratulations!")
#         print(f"You managed to guess it in {guesses} tries")
#         if guesses < 5:
#             print("You are lucky today!")
#         print("Number of guess is {0}, low is {1}, high is {2}, target number is {3}, user guess is {4}".format(guesses,low,high,target_number,guess))
#         break


import random

def play_game():
    user_score = 0
    comp_score = 0
    tie = 0
    while True:
        user_action = input("Enter a choice (rock , paper, scissors):").lower()
        possible_actions = ["rock", "paper", "scissors"]
        if user_action not in possible_actions:
            print("Invalid option. Please choose from 'rock', 'paper', or 'scissors' . ")
        else:
            computer_action = random.choice(possible_actions)
            print(f"\n You choose {user_action}, computer choose {computer_action}.\n")


            if user_action == computer_action:
                tie += 1
                print(f"Both players selected {user_action}. It's a tie!!")
            elif user_action == "rock":
                if computer_action == "scissors":
                    print("Rock smashes scissors! You win!!")
                    user_score += 1
                else:
                    
                    print("Paper covers rock! You lose.")
                    comp_score += 1
            elif user_action == "paper":
                if computer_action == "rock":
                    print("Paper covers rock! You win!!")
                    user_score += 1
                else: 
                    print("Scissors cuts paper! You lose. ")
                    comp_score += 1
            elif user_action == "scissors":
                if computer_action == "paper":
                    print("Scissors cuts paper! You win!!")
                    user_score += 1
                else:
                    print("Rock smashes scissors! You loose. ")
                    comp_score += 1
            print(f"Your score: {user_score}, Computer score: {comp_score},Tie: {tie}")

            while True:
                play_again = input("Play again? (y/n):").lower()
                if play_again in ["n","no"]:
                    print("Exiting the game.")
                    return
                elif play_again not in ["y","yes"]:
                    print("Invalid input. Please enter 'y' (yes) or 'n'  (no). ")
                else:
                    break


                