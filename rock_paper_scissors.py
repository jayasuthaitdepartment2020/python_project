import random
'''user_wins = 0
computer_win = 0
options = ["rock", "paper", "scissors"]
while True:
    user_input = input("type Rock/Paper/Scissors or Q to quit : ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Enter the correct option, you entered something wrong")
        continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("computer picked ", computer_pick+".")
    if user_input == "rock" and computer_pick == "scissors":
        print("You wins")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You wins")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You wins")
        user_wins += 1
    elif (user_input == "paper" and computer_pick == "paper") or (user_input == "rock" and computer_pick == "rock") or (user_input == "scissors" and computer_pick == "scissors"):
        print("game draw, no points  ")
    else:
        print("you lost")
        computer_win += 1
print("You won ", user_wins, " times")
print("computer won ", computer_win, " times")
print("Good bye")
'''
print("Welcome to my Rock/Paper/Scissors")
print("Lets Go :)")
print('''Instruction :
      * The rules of the game is given below
      * If you choose rock computer choose scissors in the case you win
      * If you choose scissors and computer choose paper in that case you win
      * If you choose paper and computer choose rock in that case you win
      * If both choose same game is draw
      * Other than these condition computer wins
      * Good luck
      ''')
options = ["rock", "paper", "scissors"]
user_win = 0
computer_win = 0
while True:
    user_input = input("Type what you chosen rock/paper/scissors : ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("please choose correct option,you type something wrong ")
        break
    random_number = random.randint(0, 2)
    comp_pick = options[random_number]
    print("computer picks ", comp_pick+".")
    if (user_input == "rock" and comp_pick == "scissors") or (user_input == "scissors" and comp_pick == "paper") or user_input == "paper" and comp_pick == "rock":
        print("You wins")
        user_win += 1
    elif (user_input == "paper" and comp_pick == "paper") or (user_input == "rock" and comp_pick == "rock") or (user_input == "scissors" and comp_pick == "scissors"):
        print("game draw, no points  ")
    else:
        print("you lost")
        computer_win += 1
print("You won ", user_win, " times")
print("computer won ", computer_win, " times")
print("Good bye")
