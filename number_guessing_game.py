import random
'''# randrange is (1,10) is start with 1 and end with 9
# randint is(1,10) is start with 1 and end with 10 also we don't need start
#r= random.randrange(1, 10)
# r1=random.randint(10)
# print(r)
top_range = input("Enter the number of guess range : ")
if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("please enter the number larger than 0")
        quit()
else:
    print("Hey enter the number , you entered something wrong")
    quit()
random_number = random.randint(0, top_range)
gus = 0
while True:
    guess = input("guess the number : ")
    gus += 1
    if guess.isdigit():
        guess = int(guess)
    else:
        print("please enter the number larger than 0")
        continue
    if guess == random_number:
        print("you got it")
        break
    elif guess > random_number:
        print("you were above the number")
    else:
        print("you were below the number")
print("you find the guessing number in " + str(gus) + " guesses")


# random_number = random.randint(0, top_range)
# print(random_number)
'''
print("WELCOME TO MY NUMBER GUESSING GAME")
print("LETS GO :)")
print('''Instruction:
      welcome again!!!
      * the range of the number start with 0 and range end your choice
      * there is no limitation of the guesses
      * above and below instruction also given in this game
      * Good Luck ''')
top_range = input("Enter the range of the number : ")
if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("The range of the number is always above 0 \nTry again")
        quit()
else:
    print("please enter the number, you entered something wrong \nTry again")
    quit()
random_number = random.randint(0, top_range)
guesses = 0
while True:
    guessing_number = input("Enter the guessing number : ")
    guesses += 1
    if guessing_number.isdigit():
        guessing_number = int(guessing_number)
        if guessing_number < 0:
            print("The range of the number is always above 0 ")
            continue
    else:
        print("please enter the number, you entered something wrong \nTry again")
        continue
    if guessing_number == random_number:
        print("You got it!")
        break
    elif guessing_number > random_number:
        print("you were above the number")
    else:
        print("You were below the number")
print("You got the answer is " + str(guesses) + " guesses")
