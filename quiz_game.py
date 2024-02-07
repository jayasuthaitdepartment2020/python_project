
# LEARNING QUIZ GAME
# MY OWN PROJECT FROM THE LEARNING IS BELOW LINE 50
#just change and commit it and check it
'''
print("Welcome to my Quiz game")
playing = input("DO you want to play the game? ")
# print(playing)
if playing.lower() != "yes":
    quit()
print("Okey! Lets play :)")

score = 0


ans = input("what does CPU stands for ? ")
if ans.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")
ans = input("what does GPU stands for ? ")
if ans.lower() == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")
ans = input("what does RAM stands for ? ")
if ans.lower() == "random access memory":
    print("correct")
    score += 1
else:
    print("incorrect")
ans = input("what does ROM stands for ? ")
if ans.lower() == "read only memory":
    print("correct")
    score += 1
else:
    print("incorrect")
print("you got " + str(score)+" questions correct!")
print("you got " + str(score/4*100)+" %")
'''
print('''
    WELCOME
    Instruction:
      * This game consist of 4 questions,each questions have 1 marks
      * end of the game mark and answer will be provides''')
print("Welcome to my Quiz game")
playing = input("DO you want to play the game? ")
# print(playing)
if playing.lower() != "yes":
    quit()
print("Okey! Lets play :)")

score = 0
L = ["central processing unit", "graphics processing unit",
     "random access memory", "read only memory"]
ans = input("what does CPU stands for ? ")
if ans.lower() == L[0]:
    # print("correct")
    score += 1
ans = input("what does GPU stands for ? ")
if ans.lower() == L[1]:
    # print("correct")
    score += 1
ans = input("what does RAM stands for ? ")
if ans.lower() == L[2]:
    # print("correct")
    score += 1
ans = input("what does ROM stands for ? ")
if ans.lower() == L[3]:
    # print("correct")
    score += 1
print("you got " + str(score)+" questions correct!")
print("you got " + str(score/4*100)+" %")
if score == 4:
    print("You Got It :)")
else:
    n = 1
    final = input("Do you want to know the answers of the questions? ")
    if final.lower() == "yes":
        for i in L:
            print(str(n)+". " + i)
            n += 1
