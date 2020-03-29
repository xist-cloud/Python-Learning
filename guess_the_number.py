import random
import os
import time
os.system('cls')
r= random.randint(1,20) #generates random number between 1 to and 20
r=int(r)
turns = 5
while turns > 0:
    print("Turns::",turns)
    guess = input("Guess the number between 1 and 20:: ")
    guess=int(guess)
    if r==guess:
        print("Correct guess")
        time.sleep(0.5)
        break
    else:
        print("Wrong")
        turns -= 1
        if r<guess:
            print("Guess was high")
        else:
            print("Guess was low")
    time.sleep(0.5)
    os.system('cls')
    if turns == 0:
        print("Out of turns")
        print("Correct answer was", r)
