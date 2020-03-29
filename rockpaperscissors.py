import random
import os
import time
choose = ['rock','paper','scissors']
cpu_choice = choose.index(random.choice(choose))
user = input("Enter choice {}:: ".format(choose))
os.system('cls')
if user not in choose:
    print("Wrong input")
else:
    user=choose.index(user)
    print("Computer:: {}".format(choose[cpu_choice]))
    print("User:: {}".format(choose[user]))
    if user == cpu_choice:
        print("Draw")
    else:
        if cpu_choice<user and user!=0 and cpu_choice!=2:
            print("User wins")
        else:
            print("CPU wins")
time.sleep(3)
