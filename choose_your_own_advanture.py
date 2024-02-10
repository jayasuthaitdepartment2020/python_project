'''name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swam acrross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)
'''
print("Welcome to my choose your own advanture game")

print('''Intruction :
      * In this game you can choose your own path
      *You can't come back, other than you lost
      * you can choose the correct path at the end you get your destiny
      * you choose the wrong path the game will be end
      *Game name find my prince named raja ''')
name = input("May I ask your your name : ")
print("Welcome", name, "to my advanture game")
print("Lets Go :)")
while True:
    op = input("Do you want to play the game (yes/no) ").lower()
    if op == "no":
        break

    else:
        ans = input(
            "nee eppo oru forest la erukka you want (get out /stay)").lower()
        if ans == "get out":
            ans = input(
                "you pick the road ,there is a car coming to you and a cycle besides you (car/cycle) : ").lower()
            if ans == "cycle":
                ans = input(
                    "you travelling using the cycle,road side oru cat adippattu erukku(first aid/go) ").lower()
                if ans == "first aid":
                    ans = input(
                        "you first aid the cat and travel with it,you are starving(eat/travel) ").lower()
                    if ans == "eat":
                        ans = input(
                            "In that eating place you see the beautiful young man ,He went to speak to you (speak/not speak) ").lower()
                        if ans == "speak":
                            ans = input(
                                "He speak to you and thanks to you(asked why/or not) ").lower()
                            if ans == "asked why":
                                ans = input(
                                    "He say this is my cat to saving my cat i say thanks to you (asked name/or not) ").lower()
                                if ans == "asked name":
                                    ans = input("what is your name ? ").lower()
                                    if ans == "raja":
                                        print("You win")
                                elif ans == "or not":
                                    print("You Lost your prince")
                                else:
                                    print("You choosed something wrong ")
                                    print("You Lost")
                            elif ans == "or not":
                                print("You Lost your prince")
                            else:
                                print("You choosed something wrong ")
                                print("You Lost")
                        elif ans == "not speak":
                            print("You Lost your prince")
                        else:
                            print("You choosed something wrong ")
                            print("You Lost")

                    elif ans == "travel":
                        print("You Lost,you are collapsed")
                    else:
                        print("You choosed something wrong ")
                        print("You Lost")
                elif ans == "go":
                    print("You Lost,your lack of kindness")
                else:
                    print("You choosed something wrong ")
                    print("You Lost")

            elif ans == "car":
                print("you pick the stranger is car \n You Lost")
            else:
                print("You choosed something wrong ")
                print("You Lost")

        elif ans == "stay":
            ans = input(
                "You meet the dog ,it asked for the help(help/decline) ").lower()
            if ans == "help":
                ans = input(
                    "it asked you to follow the dog(follow/not) ").lower()
                if ans == "follow":
                    ans = input(
                        "you following the dog,its came to a house(enter/or not) ").lower()
                    if ans == "enter":
                        ans = input(
                            "there is a lady is suffering you (help/or not) ").lower()
                        if ans == "help":
                            ans = input(
                                "you hepled the lady and get out walk in the road,you see the young man he went to speak to you(speak/not speak)").lower()
                            if ans == "speak":
                                ans = input(
                                    "he speak and thanks to you(ask why/or not) ").lower()
                                if ans == "ask why":
                                    ans = input(
                                        "he say you saved him mom(asked name/or not) ").lower()
                                    if ans == "asked name":
                                        ans = input(
                                            "Whats your name ? ").lower()
                                        if ans == "raja":
                                            print(
                                                "You Won,Finally you find your prince")
                                    elif ans == "or not":
                                        print("You Lost,he is the prince")
                                    else:
                                        print("You choosed something wrong ")
                                        print("You Lost")
                                elif ans == "or not":
                                    print("You Lost,he is the prince")
                                else:
                                    print("You choosed something wrong ")
                                    print("You Lost")
                            elif ans == "not speak":
                                print("You Lost your prince")
                            else:
                                print("You choosed something wrong ")
                                print("You Lost")
                        elif ans == "or not":
                            print("You Lost,she is a prince mom")
                        else:
                            print("You choosed something wrong ")
                            print("You Lost")
                    elif ans == "or not":
                        print("You Lost,dog is a prince dog")
                    else:
                        print("You choosed something wrong ")
                        print("You Lost")
                elif ans == "reject":
                    print("You Lost ,you stuck in the forest")
                else:
                    print("You choosed something wrong ")
                    print("You Lost")
            elif ans == "decline":
                print("You Lost ,you stuck in the forest")
            else:
                print("You choosed something wrong ")
                print("You Lost")
print("Thank you for playing this game ")
''' ans = input(
                "You meet the old man in the forest,he asked help to you pick the fruit (help/decline) ")
            if ans == "help":
                ans = input(
                    "for the kind help ,he asked to you to eat with there family(accept/reject) ").lower()
                if ans == "accept":
                    ans = input(
                        "you joined there family.In that place you meet the beautiful young man(asked name/or not) ").lower()
                    if ans == "asked name":
                        ans = input("What is your name ? ").lower()
                        if ans == "raja":
                            print("You won,Finally you find your prince")
                    elif ans == "or not":
                        print("You Lost,he is the prince")
                    else:
                        print("You choosed something wrong ")
                        print("You Lost")
                elif ans == "reject":
                    print("You Lost ,you stuck in the forest")
                else:
                    print("You choosed something wrong ")
                    print("You Lost")
            elif ans == "decline":
                print("You Lost ,you stuck in the forest")
            else:
                print("You choosed something wrong ")
                print("You Lost")
'''
