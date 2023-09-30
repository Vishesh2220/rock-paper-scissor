import random
option=("rock","paper","scissor")
player=None
computer=random.choice(option)
running=True
while running:
    player=None
    computer=random.choice(option)
    while player not in option:
        player=input('enter a choice(rock,paper ,scissor):-')
        if(player==computer):
            print('its a tie!')
        elif(player=="paper" and computer=="rock"):
            print("computer choice is ",computer)
            print("you win!")
        elif(player=="scissor" and computer=="paper"):
            print("computer choice is ",computer)
            print("you win!")
        elif(player=="rock" and computer=="scissor"):
            print("computer choice is ",computer)
            print("you win!")
        else:
            print("computer choice is ",computer)
            print("you loss!")
            a=input("do you want to play (y/n)").lower()
            if not a=="y":
                running=False
                print('thanks for playing!')




