import random
print("Let's plap a guessing game with me to pass time!")
random_number=random.randint(1,100)
guess_attempts=0
while True:
    guess=int(input("Close your eyes and think of random between 1 to 100 number:"))
    guess_attempts=+1
    if guess==random_number:
        print("Yay!you got it right")
        break
    elif guess<random_number:
            print("Try for bigger number")
    else:
        print("Try for lower number ")
                

