import random
playing=True
number=str(random.randint(0,9))
print("i will generate a random number 0 -> 9")
("this game will only end if you guess the correct number")
while playing:
    guess=input("give me your best guess \n")
    if number==guess:
        print("you win the game")
        print("the number was: ",number)
        break
    else:
        print("your guess is wrong,try it again \n")