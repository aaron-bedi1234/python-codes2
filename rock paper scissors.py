import random
yourscore=0
computerscore=0
while True:
    user_action=input("enter a choice rock paper or scissors")
    possible_actions=["rock","paper","scissors"]
    computer_action=random.choice(possible_actions)
    print(f"\nyou chose {user_action} ,computer chose {computer_action} \n")
    if user_action==computer_action:
        print(f"both players selected {user_action} ,it is a tie")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("rock smashed scissors,you win")
            yourscore=+1
        else: 
            print("paper covers rock you lose")
            computerscore+1
    elif user_action=="paper":
        if computer_action=="rock":
            print("paper covers rock you win")
            yourscore+1
        else:
            print("scissors cuts paper you lose")
            computerscore+1
    elif user_action=="scissors":
        if computer_action=="paper":
            print("scissors cuts paper you win")
            yourscore+1
        else:
            print("rock smashes scissors you lose")
            computerscore+1
            play_again=input("play again? y or n")
            if play_again!="y":
                break
if yourscore>computerscore:
    print(f"you won {yourscore-computerscore} more times that the computer")
elif computerscore>yourscore:
    print(f"computer won {computerscore-yourscore} more times than you")
else:
    print("both of you have tied")