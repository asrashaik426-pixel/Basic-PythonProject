import random
print("\n Let's play rock,paper and scissors for fun")
selection=["rock","paper","scissors"]
user_pick=input("enter your choice rock or paper or scissors:")
computer=random.choice(selection)

if user_pick==computer:
    print("tie!how boring")
elif(user_pick=="rock" and computer=="paper")or\
    (user_pick=="scissors" and computer=="rock")or\
    (user_pick=="paper" and computer=="scissors"):
    print("computer wins")
else:
    print("you win")

        

        

    
    
